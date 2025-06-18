from tkinter.filedialog import askopenfilename
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Fungsi Cari Invers Modulo 
def modinv(a, m):
    a = int(a)
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError(f"Tidak ada invers untuk {a} modulo {m}")

# Invers Table 
modulo = 256
inverse_table = np.zeros(modulo, dtype=np.uint8)
for a in range(1, modulo):
    try:
        inverse_table[a] = modinv(a, modulo)
    except ValueError:
        inverse_table[a] = 0

# Pilih File Gambar
filepath = askopenfilename(title="Pilih gambar", filetypes=[("Image files", "*.png *.jpg *.jpeg")])
img = Image.open(filepath)
if img.mode != 'RGB':
    img = img.convert('RGB')

arr = np.array(img)
shape = arr.shape
height, width, channels = shape
size = height * width

# Fungsi generate kunci valid (ganjil)
def generate_keys():
    return np.random.choice(np.arange(1, 256, 2), size=size).astype(np.uint8).reshape((height, width))

# Enkripsi per channel
def encrypt_channel(channel, key):
    encrypted = (channel.astype(np.uint16) * key.astype(np.uint16)) % 256
    return encrypted.astype(np.uint8)

# Dekripsi per channel
def decrypt_channel(channel, key):
    key_flat = key.flatten()
    key_inv = inverse_table[key_flat].reshape((height, width))
    decrypted = (channel.astype(np.uint16) * key_inv.astype(np.uint16)) % 256
    return decrypted.astype(np.uint8)

# Generate key dan permutasi
key_R = generate_keys()
key_G = generate_keys()
key_B = generate_keys()
perm_indices = np.random.permutation(size)
inverse_perm = np.argsort(perm_indices)

# Pisah channel RGB
R, G, B = arr[:,:,0], arr[:,:,1], arr[:,:,2]

# Enkripsi
R_enc = encrypt_channel(R, key_R).flatten()[perm_indices].reshape((height, width))
G_enc = encrypt_channel(G, key_G).flatten()[perm_indices].reshape((height, width))
B_enc = encrypt_channel(B, key_B).flatten()[perm_indices].reshape((height, width))
enc_image = np.stack((R_enc, G_enc, B_enc), axis=2)

# Dekripsi
R_unshuffled = R_enc.flatten()[inverse_perm].reshape((height, width))
G_unshuffled = G_enc.flatten()[inverse_perm].reshape((height, width))
B_unshuffled = B_enc.flatten()[inverse_perm].reshape((height, width))

R_dec = decrypt_channel(R_unshuffled, key_R)
G_dec = decrypt_channel(G_unshuffled, key_G)
B_dec = decrypt_channel(B_unshuffled, key_B)
dec_image = np.stack((R_dec, G_dec, B_dec), axis=2)

# ====================== TAMPILKAN HASIL ===================================
plt.figure(figsize=(15, 5))
plt.suptitle("Proses Enkripsi dan Dekripsi Citra", fontsize=18, fontweight='bold')

plt.subplot(1, 3, 1)
plt.imshow(arr)
plt.title("Gambar Asli", fontweight='bold')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(enc_image)
plt.title("Terenkripsi", fontweight='bold')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(dec_image)
plt.title("Terdekripsi", fontweight='bold')
plt.axis('off')

plt.tight_layout()
plt.show()

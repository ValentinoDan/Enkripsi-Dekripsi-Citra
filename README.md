# 🔒 Enkripsi-Dekripsi Citra RGB dengan Perkalian Modular dan Permutasi Piksel

Proyek Python ini mengimplementasikan proses enkripsi dan dekripsi citra RGB menggunakan kombinasi aritmetika modular dan permutasi posisi piksel. Metode ini cocok digunakan sebagai bahan pembelajaran, tugas akhir, atau penelitian di bidang pengolahan citra dan kriptografi sederhana.

## 📌 Fitur

- Mendukung citra RGB (format `.png`, `.jpg`, `.jpeg`)
- Enkripsi dilakukan secara terpisah untuk kanal R, G, dan B
- Menggunakan perkalian modular (mod 256) untuk mengacak nilai intensitas piksel
- Mengacak posisi piksel dengan permutasi acak
- Mengembalikan citra asli dengan proses pembalikan penuh
- Menampilkan visualisasi tahap: citra asli, terenkripsi, dan terdekripsi

## 🧠 Cara Kerja

### 🔐 Enkripsi

1. **Pembuatan Kunci**  
   Menghasilkan nilai kunci berupa bilangan ganjil acak dari 1 hingga 255. Nilai ganjil dipilih karena memiliki invers modulo 256, yang diperlukan untuk proses dekripsi.

2. **Perkalian Modular**  
   Setiap nilai piksel pada kanal R, G, dan B dikalikan dengan nilai kunci masing-masing, kemudian diambil hasil mod 256 untuk menjaga rentang nilai 0–255.

3. **Permutasi Piksel**  
   Posisi piksel diacak menggunakan `np.random.permutation` untuk menyembunyikan struktur spasial gambar.

4. **Penggabungan Kembali**  
   Kanal R, G, dan B yang telah dienkripsi digabungkan kembali menggunakan `np.stack(..., axis=2)` menjadi citra RGB utuh.

### 🔓 Dekripsi

1. **Pembalikan Permutasi**  
   Indeks permutasi dibalik menggunakan `np.argsort(...)` untuk mengembalikan posisi piksel ke urutan semula.

2. **Perkalian dengan Invers Modular**  
   Setiap piksel dikalikan dengan invers dari kunci yang digunakan saat enkripsi, sehingga nilai asli dapat dipulihkan.

3. **Rekonstruksi Citra**  
   Kanal R, G, dan B hasil dekripsi digabungkan menjadi citra RGB akhir yang identik dengan citra asli.

## 📁 Struktur File
```bash
├── Enkripsi-Dekripsi-Citra.py
├── Image.png
└── README.md
```       

## ▶️ Cara Menjalankan

1. Clone repositori ini:
```bash
git clone https://github.com/ValentinoDan/Enkripsi-Dekripsi-Citra.git
```
2. Install dependensi berikut :
``` bash
pip install numpy pillow matplotlib
```
3. Jalankan program
``` bash
python Enkripsi-Dekripsi-Citra.py
```
## 📸 Contoh Output

Hasil enkripsi dan dekripsi citra RGB:

![Hasil Enkripsi dan Dekripsi](Image.png)






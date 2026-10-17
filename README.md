# Pertemuan 7 — Fungsi dalam Python

## Identitas
- Nama: Aulia Safitri
- NIM: 2225250190
- Kelas: 3B
- Mata Kuliah: Algoritma dan Pemrograman

## Tujuan
Mempelajari penggunaan fungsi, parameter, return value, dan scope dalam Python.

## Daftar File
1. `latihan/01_salam.py`
2. `latihan/02_luas_persegi_panjang.py`
3. `latihan/03_jumlah_n.py`
4. `latihan/04_statistik_sederhana.py`
5. `latihan/05_scope.py`
6. `praktik/utilitas_matematika.py`

## Cara Menjalankan Program
1. Buka folder tugas di Visual Studio Code.
2. Buka file Python yang ingin dijalankan.
3. Jalankan program melalui terminal menggunakan perintah `python nama_file.py`.

## Pengujian Program
- Luas persegi panjang dengan panjang 8 dan lebar 5 menghasilkan 40.
- Luas segitiga dengan alas 10 dan tinggi 6 menghasilkan 30.
- Jumlah bilangan dari 1 sampai 10 menghasilkan 55.
- Faktorial dari 5 menghasilkan 120.
- Faktorial dari 0 menghasilkan 1.

## Kesimpulan
Fungsi dalam Python membantu membuat program lebih terstruktur, mudah dibaca, dan dapat digunakan kembali.

## Refleksi
Saya belajar menggunakan fungsi, parameter, return value, dan scope dalam Python. Saya juga belajar menguji program dan mengunggah tugas ke GitHub.

## Kuis Formatif Pertemuan 7

### 1. Apa fungsi kata kunci def dalam Python?
Kata kunci `def` digunakan untuk mendefinisikan atau membuat fungsi dalam Python. Fungsi membantu membagi program menjadi bagian-bagian kecil yang dapat digunakan kembali.

### 2. Apa perbedaan parameter dan argumen?
Parameter adalah variabel yang ditulis pada definisi fungsi untuk menerima data. Argumen adalah nilai yang diberikan ketika fungsi dipanggil.

### 3. Kapan return lebih tepat daripada print?
`return` lebih tepat digunakan ketika hasil fungsi perlu disimpan atau digunakan kembali dalam perhitungan lain. Sementara itu, `print` digunakan untuk menampilkan informasi ke layar.

### 4. Apa nilai variabel x pada kode x = kuadrat(4) jika kuadrat mengembalikan x*x?
Nilai variabel `x` adalah 16 karena fungsi menghitung 4 × 4 dan mengembalikan hasilnya.

### 5. Mengapa variabel lokal sebaiknya tidak bergantung pada perubahan dari luar fungsi?
Variabel lokal membantu menjaga proses di dalam fungsi agar lebih terstruktur dan mengurangi risiko perubahan nilai yang tidak diinginkan. Hal ini juga membuat fungsi lebih mudah diuji dan diperbaiki.

### 6. Apa yang terjadi jika fungsi memerlukan dua parameter tetapi hanya diberi satu argumen?
Python akan menghasilkan kesalahan `TypeError` karena jumlah argumen yang diberikan tidak sesuai dengan jumlah parameter yang diwajibkan.

### 7. Bagaimana cara memakai nilai return dalam perhitungan lain?
Nilai `return` dapat disimpan dalam variabel atau langsung digunakan dalam ekspresi dan perhitungan lain.

### 8. Apa perbedaan Step Into dan Step Over saat debugging fungsi di VS Code?
Step Into digunakan untuk masuk ke dalam fungsi yang dipanggil dan menelusuri perintah di dalamnya. Step Over digunakan untuk menjalankan satu baris kode tanpa masuk ke dalam fungsi yang dipanggil pada baris tersebut.

### 9. Mengapa modularisasi membantu pengujian program?
Modularisasi membantu pengujian karena program dibagi menjadi fungsi-fungsi kecil dengan tugas yang jelas. Setiap fungsi dapat diuji secara terpisah sehingga kesalahan lebih mudah ditemukan dan diperbaiki.

### 10. Perintah Git apa yang mengirim commit lokal ke GitHub setelah remote sudah terhubung?
Perintah yang digunakan adalah `git push`. Perintah tersebut mengirim commit lokal ke repositori GitHub yang sudah terhubung melalui remote.

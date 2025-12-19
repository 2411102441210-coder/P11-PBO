# Laporan Penelusuran Bug (Debugging Report) - Pertemuan 14

## 1. Identifikasi Masalah
Setelah dilakukan pengujian awal, ditemukan bahwa fungsi `hitung_diskon` memberikan hasil yang tidak sesuai ekspektasi. Harga akhir jauh lebih tinggi dari yang seharusnya (misal: input 1000 diskon 10% menghasilkan 990.0, padahal seharusnya 900.0).

## 2. Langkah Penelusuran (Trace Log)
Penelusuran dilakukan menggunakan debugger `pdb` dengan langkah sebagai berikut:
1. Memasang `pdb.set_trace()` di dalam method `hitung_diskon`.
2. Menjalankan perintah `n` (next) untuk melewati baris kalkulasi.
3. Memeriksa variabel `jumlah_diskon` dengan perintah `p jumlah_diskon`, didapatkan nilai `100.0` (Benar).
4. Memeriksa variabel `harga_akhir` sebelum fungsi berakhir.

## 3. Akar Masalah (Root Cause)
Berdasarkan pemeriksaan nilai variabel pada saat runtime, ditemukan bug logika pada baris:
`harga_akhir += harga_akhir * 0.1`
Baris ini secara tidak sengaja menambahkan PPN 10% ke harga yang sudah didiskon, sehingga harga akhir menjadi salah.

## 4. Solusi dan Verifikasi
- **Solusi:** Menghapus/memberi komentar pada baris penambahan PPN tersebut.
- **Verifikasi:** Setelah baris dihapus, pengujian menggunakan `unittest` memberikan hasil **OK**.
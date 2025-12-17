# P11-PBO
**Nama:** [Raisyi Salsabila]
**NIM:** [2411102441210]

## Analisis
Berdasarkan modul praktikum, kode awal punya beberapa pelanggaran prinsip desain:

1. **Single Responsibility Principle (SRP):**
   - **Pelanggaran:** Kelas `OrderManager` menangani proses pembayaran sekaligus pengiriman notifikasi.
   - **Dampak:** Jika ada perubahan pada sistem notifikasi, kita harus memodifikasi kelas yang juga mengatur pembayaran.

2. **Open/Closed Principle (OCP):**
   - **Pelanggaran:** Metode pembayaran menggunakan blok `if/else` yang kaku (hardcoded).
   - **Dampak:** Untuk menambah metode pembayaran baru (seperti QRIS atau e-wallet), kita wajib mengubah kode di dalam kelas utama, yang berisiko merusak logika yang sudah stabil.

3. **Dependency Inversion Principle (DIP):**
   - **Pelanggaran:** Kelas tingkat tinggi bergantung langsung pada implementasi konkrit metode pembayaran.
   - **Dampak:** Kode menjadi kaku karena modul logika bisnis terikat langsung dengan detail low-level.

## Solusi Refactoring
Setelah dilakukan refactoring di file `refactor_solid.py` dan `latihan_mandiri.py`:
- **SRP:** Tanggung jawab dipisahkan ke kelas `IPaymentProcessor` dan `INotificationService`
- **OCP/DIP:** Menggunakan abstraksi (Abstract Class) dan *Dependency Injection* sehingga fitur baru bisa ditambah tanpa mengubah kode yang sudah ada.

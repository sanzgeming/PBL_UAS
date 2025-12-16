# PBL — Sistem Pengelolaan Nilai UKM/Lomba

Ringkasan singkat:  
Aplikasi CLI Python untuk mengelola data peserta lomba / UKM. Menyediakan fitur tambah, tampil, cari, edit, dan hapus peserta. Skor tiap peserta terdiri dari 3 ronde; total dan peringkat dihitung sesuai ketentuan.

## Fitur utama
- Menambah peserta (validasi nama, tim A/B/C, skor 0–100)
- Menampilkan semua peserta
- Menampilkan peserta per tim (nested loop)
- Mencari peserta berdasarkan nama atau tim
- Mengedit peserta (nama/tim/skor dengan validasi)
- Menghapus peserta dengan konfirmasi
- Penentuan peringkat:
  - Total ≥ 250 → Juara
  - 200–249 → Lolos
  - <200 → Tidak Lolos

## Struktur proyek
```
PBL/
├── data/
│   └── data.py
├── peserta.py
├── skor.py
├── input.py
├── display.py
├── edit.py
├── delete.py
├── cari_peserta.py
├── main.py
└── README.md
```

> Catatan: beberapa nama fungsi/field diimplementasikan dengan nama bahasa Indonesia (mis. `nama`, `tim`, `r1`/`r2`/`r3`) untuk konsistensi.

## Cara menjalankan (Windows)
1. Pastikan Python 3 terpasang.
2. Buka terminal di folder proyek:
   cd "C:\Users\Insan Nur Rifai H\OneDrive\Documents\ALGORITMA DAN PEMROGRAMAN\PBL"
3. Jalankan:
   py main.py

Menu interaktif akan muncul; pilih opsi sesuai nomor.

## Contoh alur penggunaan
- Pilih 3 untuk menambah peserta → isi nama (tidak boleh angka), pilih tim (A/B/C), masukkan skor ronde (0–100).
- Pilih 1 untuk menampilkan semua peserta.
- Pilih 2 untuk tampilan berurut per tim (nested loop).
- Pilih 4 untuk mencari berdasarkan nama atau tim.
- Pilih 5 untuk edit, 6 untuk hapus (dengan konfirmasi).

## Validasi & aturan penting
- Nama tidak boleh kosong atau berisi angka.
- Tim terbatas pada A, B, C.
- Skor tiap ronde integer antara 0 dan 100.
- Saat menambah peserta, input yang tidak valid akan diminta ulang (loop).

## Pengembangan & testing
- Untuk memisahkan logika dari I/O, gunakan fungsi di modul masing‑masing (sudah dipisahkan).
- Disarankan menulis unit test untuk:
  - fungsi perhitungan skor & peringkat di `skor.py`
  - fungsi tambah / edit / hapus di `peserta.py`
  - pencarian di `cari_peserta.py`
- Struktur untuk test: buat folder `tests/` dan gunakan pytest.

## Tips perbaikan berikutnya
- Simpan data ke file JSON/CSV sehingga perubahan persist.
- Tambah export (CSV) dan import.
- Tambah unit test otomatis dan CI ringan (GitHub Actions).

## Lisensi
- Sesuaikan lisensi proyek (mis. MIT) bila ingin membagikan atau publikasi.

Jika mau, saya bisa:
- Membuat file README.md ini di folder Anda.
- Menambahkan contoh unit test (pytest) untuk fungsi utama.
- Menambahkan penyimpanan data (JSON) agar data persist antar sesi.

```<!-- filepath: c:\Users\Insan Nur Rifai H\OneDrive\Documents\ALGORITMA DAN PEMROGRAMAN\PBL\README.md -->

# PBL — Sistem Pengelolaan Nilai UKM/Lomba

Ringkasan singkat:  
Aplikasi CLI Python untuk mengelola data peserta lomba / UKM. Menyediakan fitur tambah, tampil, cari, edit, dan hapus peserta. Skor tiap peserta terdiri dari 3 ronde; total dan peringkat dihitung sesuai ketentuan.

## Fitur utama
- Menambah peserta (validasi nama, tim A/B/C, skor 0–100)
- Menampilkan semua peserta
- Menampilkan peserta per tim (nested loop)
- Mencari peserta berdasarkan nama atau tim
- Mengedit peserta (nama/tim/skor dengan validasi)
- Menghapus peserta dengan konfirmasi
- Penentuan peringkat:
  - Total ≥ 250 → Juara
  - 200–249 → Lolos
  - <200 → Tidak Lolos

## Struktur proyek
- data/
  - data.py — data awal / fungsi penyedia data contoh
- peserta.py — manajemen peserta (tambah, edit, delete helpers)
- skor.py — fungsi perhitungan skor dan penentuan peringkat
- input.py — helper validasi input (nama, tim, skor, konfirmasi)
- display.py — fungsi format & tampilan daftar peserta / per tim
- edit.py — UI edit peserta (interaktif)
- delete.py — UI hapus peserta (interaktif)
- cari_peserta.py — utility pencarian dan tampilan hasil
- main.py — program utama (menu loop)
- README.md — dokumentasi (file ini)

> Catatan: beberapa nama fungsi/field diimplementasikan dengan nama bahasa Indonesia (mis. `nama`, `tim`, `r1`/`r2`/`r3`) untuk konsistensi.

## Cara menjalankan (Windows)
1. Pastikan Python 3 terpasang.
2. Buka terminal di folder proyek:
   cd "C:\Users\Insan Nur Rifai H\OneDrive\Documents\ALGORITMA DAN PEMROGRAMAN\PBL"
3. Jalankan:
   py main.py

Menu interaktif akan muncul; pilih opsi sesuai nomor.

## Contoh alur penggunaan
- Pilih 3 untuk menambah peserta → isi nama (tidak boleh angka), pilih tim (A/B/C), masukkan skor ronde (0–100).
- Pilih 1 untuk menampilkan semua peserta.
- Pilih 2 untuk tampilan berurut per tim (nested loop).
- Pilih 4 untuk mencari berdasarkan nama atau tim.
- Pilih 5 untuk edit, 6 untuk hapus (dengan konfirmasi).

## Validasi & aturan penting
- Nama tidak boleh kosong atau berisi angka.
- Tim terbatas pada A, B, C.
- Skor tiap ronde integer antara 0 dan 100.
- Saat menambah peserta, input yang tidak valid akan diminta ulang (loop).

## Pengembangan & testing
- Untuk memisahkan logika dari I/O, gunakan fungsi di modul masing‑masing (sudah dipisahkan).
- Disarankan menulis unit test untuk:
  - fungsi perhitungan skor & peringkat di `skor.py`
  - fungsi tambah / edit / hapus di `peserta.py`
  - pencarian di `cari_peserta.py`
- Struktur untuk test: buat folder `tests/` dan gunakan pytest.

## Tips perbaikan berikutnya
- Simpan data ke file JSON/CSV sehingga perubahan persist.
- Tambah export (CSV) dan import.
- Tambah unit test otomatis dan CI ringan (GitHub Actions).

## Lisensi
- Sesuaikan lisensi proyek (mis. MIT) bila ingin membagikan atau publikasi.

Jika mau, saya bisa:
- Membuat file README.md ini di folder Anda.
- Menambahkan contoh unit test (pytest) untuk fungsi utama.
- Menambahkan penyimpanan data (JSON) agar data persist antar sesi.
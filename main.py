from peserta import tambah_peserta
from tampilan_peserta import tampil_semua
from tampilan_per_tim import tampil_per_tim
from cari_peserta import cari_peserta
from delete import delete_peserta


def main():
    print(
        """
 _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _ 
|_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_|
|_|                                                |_|
|_|  ▄▄▌ ▐ ▄▌▄▄▄ .▄▄▌   ▄▄·       • ▌ ▄ ·. ▄▄▄ .   |_|
|_|  ██· █▌▐█▀▄.▀·██•  ▐█ ▌▪▪     ·██ ▐███▪▀▄.▀·   |_|
|_|  ██▪▐█▐▐▌▐▀▀▪▄██▪  ██ ▄▄ ▄█▀▄ ▐█ ▌▐▌▐█·▐▀▀▪▄   |_|
|_|  ▐█▌██▐█▌▐█▄▄▌▐█▌▐▌▐███▌▐█▌.▐▌██ ██▌▐█▌▐█▄▄▌   |_|
|_|   ▀▀▀▀ ▀▪ ▀▀▀ .▀▀▀ ·▀▀▀  ▀█▄▀▪▀▀  █▪▀▀▀ ▀▀▀    |_|
|_| _  _  _  _  _  _  _  _  _  _  _  _  _  _  _  _ |_|
|_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_||_|
"""
    )
    while True:
        print("\n========= Sistem Pengelolaan Nilai UKM/Lomba =========")
        print("\nMenu:")
        print("1. Tambah peserta")
        print("2. Tampilkan berdasarkan tim")
        print("3. Tampilkan semua peserta")
        print("4. Cari peserta berdasarkan nama/tim")
        print("5. Hapus peserta")
        print("6. Keluar")
        choice = input("Pilih (1-6): ").strip()
        if choice == "1":
            tambah_peserta()
        elif choice == "2":
            tampil_per_tim()
        elif choice == "3":
            tampil_semua()
        elif choice == "4":
            cari_peserta()
        elif choice == "5":
            delete_peserta()
        elif choice == "6":
            print("Selesai.")
            break
        else:
            print("Pilihan tidak valid.")


main()

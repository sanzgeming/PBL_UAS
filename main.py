from peserta import tambah_peserta
from tampilan_peserta import tampil_semua
from tampilan_per_tim import tampil_per_tim
from cari_peserta import cari_peserta
from edit import edit_peserta
from delete import delete_peserta


def main():
    while True:
        print("\nMenu:")
        print("1. Tambah peserta")
        print("2. Tampilkan berdasarkan tim")
        print("3. Tampilkan semua peserta")
        print("4. Cari peserta berdasarkan nama/tim")
        print("5. Edit peserta")
        print("6. Hapus peserta")
        print("7. Keluar")
        choice = input("Pilih (1-7): ").strip()
        if choice == "1":
            tambah_peserta()
        elif choice == "2":
            tampil_per_tim()
        elif choice == "3":
            tampil_semua()
        elif choice == "4":
            cari_peserta()
        elif choice == "5":
            edit_peserta()
        elif choice == "6":
            delete_peserta()
        elif choice == "7":
            print("Selesai.")
            break
        else:
            print("Pilihan tidak valid.")
main()
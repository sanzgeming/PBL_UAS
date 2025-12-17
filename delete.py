from data.data import data_peserta
from peserta import format_peserta

peserta = data_peserta


def delete_peserta():
    key = input("Masukkan Nama/Index peserta yang akan dihapus: ").strip()
    idx = None
    if key.isdigit():
        i = int(key)
        if 0 <= i < len(peserta):
            idx = i
        else:
            print("Index di luar jangkauan.")
            return
    else:
        name_lower = key.lower()
        for i, p in enumerate(peserta):
            if p.get("nama", "").lower() == name_lower:
                idx = i
                break

    if idx is None:
        print("Peserta tidak ditemukan.")
        return

    p = peserta[idx]
    print("Peserta yang akan dihapus:")
    print(f"{'Nama':<20} | {'Tim':<10} | {'R1':>3} | {'R2':>3} | {'R3':>3} | {'Tot':>3} | {'Peringkat':^14}")
    print("-" * 78)
    print(format_peserta(p))

    confirm = (
        input("Apakah Anda yakin ingin menghapus peserta ini? (y/n): ").strip().lower()
    )
    if confirm == "y":
        del peserta[idx]
        print("Peserta berhasil dihapus.")
    else:
        print("Penghapusan dibatalkan.")
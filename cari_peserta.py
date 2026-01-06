from data.data import data_peserta
from peserta import format_peserta

peserta = data_peserta


def cari_peserta():
    found = False
    key = input("Masukkan Nama/Tim yang dicari: ")

    for p in peserta:
        if p["nama"].lower() == key.lower():
            print(
                f"{'Nama':>16}                 | {'Tim':>2}        | {'R1':>3} | {'R2':>3} | {'R3':>3} | {'Tot':>3} | {'Peringkat':^14}"
            )
            print("-" * 88)
            print("Ditemukan: ", format_peserta(p))
            print("-" * 88)
            found = True
        else:
            if p["tim"].lower() == key.lower():
                print(
                    f"{'Nama':>16}                 | {'Tim':>2}        | {'R1':>3} | {'R2':>3} | {'R3':>3} | {'Tot':>3} | {'Peringkat':^14}"
                )
                print("-" * 88)
                print("Ditemukan: ", format_peserta(p))
                print("-" * 88)
                found = True
    if not found:
        print("Data tidak ditemukan.")
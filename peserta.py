from skor import total_score, menentukan_peringkat
from data.data import data_peserta
peserta = data_peserta

def tambah_peserta():
    while True:
        nama = input("Masukkan nama peserta: ").strip()
        if not nama:
            print("Nama peserta tidak boleh kosong.")
        elif any(ch.isdigit() for ch in nama):
            print("Nama peserta tidak boleh mengandung angka.")
        else:
            break
    while True:
        tim = input("Masukkan tim peserta (A/B/C): ").strip().upper()
        if tim in ["A", "B", "C"]:
            break
        print("Tim tidak valid. Pilih salah satu: A, B, atau C.")
    while True:
        try:
            r1 = int(input("Masukkan skor ronde 1 (0-100): "))
            if r1 < 0 or r1 > 100:
                print("Nilai harus antara 0 dan 100. Silakan isi kembali.")
                continue
            break
        except ValueError:
            print("Masukkan angka yang valid (bilangan bulat).")
    while True:
        try:
            r2 = int(input("Masukkan skor ronde 2 (0-100): "))
            if r2 < 0 or r2 > 100:
                print("Nilai harus antara 0 dan 100. Silakan isi kembali.")
                continue
            break
        except ValueError:
            print("Masukkan angka yang valid (bilangan bulat).")
    while True:
        try:
            r3 = int(input("Masukkan skor ronde 3 (0-100): "))
            if r3 < 0 or r3 > 100:
                print("Nilai harus antara 0 dan 100. Silakan isi kembali.")
                continue
            break
        except ValueError:
            print("Masukkan angka yang valid (bilangan bulat).")

    peserta.append({"nama": nama, "tim": tim, "r1": r1, "r2": r2, "r3": r3})
    print("Peserta berhasil ditambahkan.")


def format_peserta(p):
    total = total_score(p)
    rank = menentukan_peringkat(total)
    return f"{p['nama']:<20} | {p['tim']:<10} | {p['r1']:>3} | {p['r2']:>3} | {p['r3']:>3} | {total:>3} | {rank:^14}"
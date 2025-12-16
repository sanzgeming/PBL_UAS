from data.data import data_peserta
from peserta import format_peserta
peserta = data_peserta

def tampil_semua():
    if not peserta:
        print("Belum ada peserta.")
        return
    print("\nDaftar Peserta:")
    print("-" * 78)
    print(f"{'Nama':<20} | {'Tim':<10} | {'R1':>3} | {'R2':>3} | {'R3':>3} | {'Tot':>3} | {'Peringkat':^14}")
    print("-" * 78)
    for p in peserta:
        print(format_peserta(p))
        print("-" * 78)
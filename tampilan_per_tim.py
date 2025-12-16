from data.data import data_peserta
from peserta import format_peserta
peserta = data_peserta

def tampil_per_tim():
    if not peserta:
        print("Belum ada peserta.")
        return
    teams = sorted({p['tim'] for p in peserta})
    print("\nDaftar peserta berdasarkan tim:")

    for team in teams:
        print(f"\nTim {team}")
        print("-" * 78)
        print(f"{'Nama':<20} | {'Tim':<10} | {'R1':>3} | {'R2':>3} | {'R3':>3} | {'Tot':>3} | {'Peringkat':^14}")
        print("-" * 78)
        for p in peserta:
            if p['tim'] == team:
                print(format_peserta(p))
                print("-" * 78)
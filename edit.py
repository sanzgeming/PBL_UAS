from data.data import data_peserta
from peserta import format_peserta
peserta = data_peserta


def edit_peserta():
    key = input("Masukkan Nama/Index peserta yang akan diedit: ").strip()
    idx = None

    # coba sebagai index
    if key.isdigit():
        i = int(key)
        if 0 <= i < len(peserta):
            idx = i
        else:
            print("Index di luar jangkauan.")
            return
    else:
        # cari berdasarkan nama (case-insensitive)
        name_lower = key.lower()
        for i, p in enumerate(peserta):
            if p.get("nama", "").lower() == name_lower:
                idx = i
                break

    if idx is None:
        print("Peserta tidak ditemukan.")
        return

    p = peserta[idx]
    print("Peserta saat ini:")
    print(format_peserta(p))
    print("Biarkan kosong jika tidak ingin mengubah.")

    # nama
    while True:
        nm = input(f"Nama ({p['nama']}): ").strip()
        if nm == "":
            name = p["nama"]
            break
        if any(ch.isdigit() for ch in nm):
            print("Nama tidak boleh mengandung angka. Silakan isi kembali.")
            continue
        name = nm
        break

    # tim
    while True:
        tm = input(f"Tim ({p['tim']}) [A/B/C]: ").strip().upper()
        if tm == "":
            team = p["tim"]
            break
        if tm in ("A", "B", "C"):
            team = tm
            break
        print(
            "Tim tidak valid. Pilih A, B, atau C atau tekan Enter untuk tidak mengubah."
        )

    # helper untuk skor
    def read_score_field(prompt, current):
        while True:
            s = input(f"{prompt} ({current}): ").strip()
            if s == "":
                return current
            try:
                v = int(s)
                if 0 <= v <= 100:
                    return v
                print("Nilai harus antara 0 dan 100.")
            except ValueError:
                print("Masukkan angka yang valid (bilangan bulat).")

    r1 = read_score_field("Skor ronde 1", p["r1"])
    r2 = read_score_field("Skor ronde 2", p["r2"])
    r3 = read_score_field("Skor ronde 3", p["r3"])

    peserta[idx].update({"nama": name, "tim": team, "r1": r1, "r2": r2, "r3": r3})
    print("Perubahan tersimpan.")
    print("Data terbaru:")
    print(format_peserta(peserta[idx]))
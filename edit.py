# from data.data import data_peserta
# from peserta import format_peserta

# peserta = data_peserta


# def input_int(prompt, default, min_val=0, max_val=100):
#     while True:
#         val = input(prompt).strip()
#         if not val:
#             return default
#         if val.isdigit() and min_val <= int(val) <= max_val:
#             return int(val)
#         print(f"Masukkan angka {min_val}-{max_val}.")


# def edit_peserta():
#     key = input("Masukkan Nama/Index peserta yang akan diedit: ").strip()
#     idx = None

#     if key.isdigit():
#         i = int(key)
#         if 0 <= i < len(peserta):
#             idx = i
#         else:
#             print("Index di luar jangkauan.")
#             return
#     else:
#         for i, p in enumerate(peserta):
#             if p["nama"].lower() == key.lower():
#                 idx = i
#                 break

#     if idx is None:
#         print("Peserta tidak ditemukan.")
#         return

#     p = peserta[idx]
#     print("\nPeserta yang akan diedit:")
#     print(f"{'Nama':<20} | {'Tim':<10} | {'R1':>3} | {'R2':>3} | {'R3':>3} | {'Tot':>3} | {'Peringkat':^14}")
#     print("-" * 78)
#     print(format_peserta(p))

#     while True:
#         new_name = input(
#             f"Nama baru (Enter untuk tetap '{p['nama']}'): "
#         ).strip()
#         if not new_name:
#             break
#         if any(ch.isdigit() for ch in new_name):
#             print("Nama tidak boleh mengandung angka.")
#         else:
#             p["nama"] = new_name
#             break

#     while True:
#         new_team = input(
#             f"Tim (A/B/C) (Enter untuk tetap '{p['tim']}'): "
#         ).strip().upper()
#         if not new_team:
#             break
#         if new_team in ["A", "B", "C"]:
#             p["tim"] = new_team
#             break
#         print("Tim tidak valid.")

#     p["r1"] = input_int(
#         f"Skor Ronde 1 (Enter untuk tetap '{p['r1']}'): ", p["r1"]
#     )
#     p["r2"] = input_int(
#         f"Skor Ronde 2 (Enter untuk tetap '{p['r2']}'): ", p["r2"]
#     )
#     p["r3"] = input_int(
#         f"Skor Ronde 3 (Enter untuk tetap '{p['r3']}'): ", p["r3"]
#     )

#     print("\nPeserta berhasil diperbarui.")
#     print("Data peserta setelah diedit:")
#     print(f"{'Nama':<20} | {'Tim':<10} | {'R1':>3} | {'R2':>3} | {'R3':>3} | {'Tot':>3} | {'Peringkat':^14}")
#     print("-" * 78)
#     print(format_peserta(p))
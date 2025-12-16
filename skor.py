def total_score(p: dict) -> int:
    return  p['r1'] + p['r2'] + p['r3']

def menentukan_peringkat(total: int) -> str:
    if total >= 250:
        return "Juara"
    elif 200 <= total <= 249:
        return "Lolos"
    else:
        return "Tidak Lolos"
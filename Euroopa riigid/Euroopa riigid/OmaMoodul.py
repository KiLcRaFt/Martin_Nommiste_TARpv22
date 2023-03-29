
def failist_to_dict(f:str):
    riik_pealinn = {}
    pealinn_riik = {}
    file=open(f, 'r', encoding="utf-8-sig")
    for line in file:
        k, v = line.strip().split('-')
        riik_pealinn[k] = v
        pealinn_riik[v] = k
    file.close()
    return riik_pealinn, pealinn_riik

def update(riik: str, pealinn: str):
    riik_pealinn.update({f"{riik}": f"{pealinn}"})
    pealinn_riik.update({f"{pealinn}": f"{riik}"})
    return riik_pealinn, pealinn_riik
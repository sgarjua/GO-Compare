
def calc_overlap_por_prote(resultados):
    overlaps = {}
    total = 0

    for prot, (gos_h, gos_f) in resultados.items():
        inter = set(gos_h) & set(gos_f)
        if inter:
            overlaps[prot] = sorted(inter)
            total += len(inter)
    return overlaps, total


def calc_overlap_por_prote(resultados_dict):
    """
    Calcula el solape de GO por proteína.
    Devuelve:
      - overlaps: dict {prote: [GO... que están en Hom y en Fan]}
      - total_solapados: número total de GO en la intersección sumando todas las proteínas
    """
    overlaps = {}
    total_solapados = 0
    for prot, (gos_h, gos_f) in resultados_dict.items():
        sh, sf = set(gos_h), set(gos_f)
        inter = sh & sf
        if inter:
            overlaps[prot] = sorted(inter)
            total_solapados += len(inter)
    return overlaps, total_solapados

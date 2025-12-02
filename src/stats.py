
from typing import Dict, Tuple

def calc_stats(resultados: dict, file, destino: int):
    id_sin_go = gos_totales = protes = 0

    for line in file:
        if not line.strip() or line.startswith("#") or "Protein-Accession" in line:
            continue

        parts = line.strip().split("\t")
        prot = parts[0].strip()
        if not prot:
            continue

        protes += 1
        resultados.setdefault(prot, [[], []])

        gos_field = parts[-1].strip()
        if "GO:" in gos_field:
            gos = [g.strip() for g in gos_field.split(",") if g.strip()]
            resultados[prot][destino] = gos
            gos_totales += len(gos)
        else:
            id_sin_go += 1

    id_con_go = protes - id_sin_go
    cobertura = (id_con_go / protes * 100) if protes else 0
    gos_por_prote = (gos_totales / protes) if protes else 0

    return protes, gos_totales, id_con_go, id_sin_go, gos_por_prote, cobertura

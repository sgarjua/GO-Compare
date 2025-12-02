
from typing import Dict, Tuple

def calc_stats(file, species: str, destino: int):
    """
    Lee un archivo de resultados y guarda los GO en resultados[prot][destino],
    donde destino=0 -> Homología, destino=1 -> FANTASIA.
    Devuelve: (protes, gos_totales, id_con_go, id_sin_go, gos_por_prote)
    """
    id_sin_go = 0
    gos_totales = 0
    protes = 0

    for line in file:
        line = line.strip()
        parts = line.split("\t")
        # saltar cabeceras o vacías
        if not line or line.startswith("#") or line.startswith("Protein-Accession"):
            continue

        prot = parts[0].strip() if parts else ""
        if not prot:
            continue
        protes += 1

        if prot not in resultados:
            resultados[prot] = [[], []]  # [hom, fan]

        gos_field = parts[-1].strip() if parts else ""
        if "GO:" in gos_field:
            gos = [g.strip() for g in gos_field.split(",") if g.strip()]
            resultados[prot][destino] = gos
            gos_totales += len(gos)
        else:
            id_sin_go += 1

    id_con_go = protes - id_sin_go
    gos_por_prote = (gos_totales / protes) if protes else 0.0
    cobertura = (id_con_go / protes) * 100
    return protes, gos_totales, id_con_go, id_sin_go, gos_por_prote, cobertura


def calc_total(outfile: Path):
    protes_h, protes_f, id_con_go_h, id_con_go_f, id_sin_go_h, id_sin_go_f, cobertura_h, cobertura_f, gos_por_prote_h, gos_por_prote_f, gos_totales_h, gos_totales_f, total_solapados, solape_h, solape_f = 0, 0 ,0 ,0 ,0 ,0 ,0, 0, 0, 0, 0, 0, 0, 0, 0
    n = 0
    with outfile.open(encoding="utf-8") as tsv:
        for line in tsv:
            line = line.strip()
            if line.startswith("Especie"):
                continue
            parts = line.split("\t")
            n += 1

            protes = parts[1].split(" | ")
            protes_h += int(protes[0])
            protes_f += int(protes[1])

            id_con_go = parts[2].split(" | ")
            id_con_go_h += int(id_con_go[0])
            id_con_go_f += int(id_con_go[1])

            id_sin_go = parts[3].split(" | ")
            id_sin_go_h += int(id_sin_go[0])
            id_sin_go_f += int(id_sin_go[1])

            cobertura = parts[4].split(" | ")
            cobertura_h += float(cobertura[0])
            cobertura_f += float(cobertura[1])

            gos_por_prote = parts[5].split(" | ")
            gos_por_prote_h += float(gos_por_prote[0])
            gos_por_prote_f += float(gos_por_prote[1])

            gos_totales = parts[6].split(" | ")
            gos_totales_h += int(gos_totales[0])
            gos_totales_f += int(gos_totales[1])

            total_solapados += int(parts[7])

            solape = parts[8].split(" | ")
            solape_h += float(solape[0])
            solape_f += float(solape[1])
    

    id_con_go_h = id_con_go_h / n
    id_con_go_f = id_con_go_f / n

    id_sin_go_h = id_sin_go_h / n
    id_sin_go_f = id_sin_go_f / n

    cobertura_h = cobertura_h / n
    cobertura_f = cobertura_f / n

    gos_por_prote_h = gos_por_prote_h / n
    gos_por_prote_f = gos_por_prote_f / n

    gos_totales_h = gos_totales_h / n
    gos_totales_f = gos_totales_f / n

    total_solapados = total_solapados / n

    solape_h = solape_h / n
    solape_f = solape_f / n

    fila = [
        "MEDIA",
        f"{protes_h} | {protes_f}",
        f"{id_con_go_h:.1f} | {id_con_go_f:.1f}",
        f"{id_sin_go_h:.1f} | {id_sin_go_f:.1f}",
        f"{cobertura_h:.1f} | {cobertura_f:.1f}",
        f"{gos_por_prote_h:.1f} | {gos_por_prote_f:.1f}",
        f"{gos_totales_h:.1f} | {gos_totales_f:.1f}",
        f"{total_solapados:.1f}",
        f"{solape_h:.1f} | {solape_f:.1f}"
        ]
    return fila, gos_totales_h, gos_totales_f, total_solapados

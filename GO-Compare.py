#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from pathlib import Path
from src.parser import parse_arguments
from src.stats import calc_stats, calc_total
from src.table import write_header, append_row
from src.overlap import calc_overlap_por_prote
from src.plotting import plot_venn


def main():

    # creamos un diccionario {secuencia: [gos homologia],[gos fantasia]}
    resultados = {}

    # diccionarios para guardar resultados de los calculos
    calculos_h = {}
    calculos_f = {}

    parser = parse_arguments()
    outfile =  Path(parser.output)
    tsv_path = Path(parser.input)
    if not tsv_path.exists():
        print(f"[ERROR] No encuentro el TSV: {tsv_path}")
        return

    cabecera = [
        "Especie",
        "Secuencias (H|F)",
        "Con GO (H|F)",
        "Sin GO (H|F)",
        "Cobertura% (H|F)",
        "Media GO/sec (H|F)",
        "GOs totales (H|F)",
        "GOs solapados (total)",
        "% (H|F)"
    ]
    write_header(outfile, cabecera)

    with tsv_path.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue

            # Formato esperado: especie<TAB>ruta_homologia<TAB>ruta_fantasia
            parts = line.split("\t")
            if len(parts) < 3:
                print(f"[WARN] Línea ignorada (esperado: especie<TAB>ruta_homologia<TAB>ruta_fantasia): {line}")
                continue

            species = parts[0].strip()
            homologia = Path(parts[1].strip())
            fantasia = Path(parts[2].strip())

            if not species or not homologia or not fantasia:
                print(f"[WARN] Falta especie o rutas en la línea: {line}")
                continue

            if not homologia.exists() or homologia.stat().st_size == 0:
                print(f"[WARN] RESULTADOS HOMOLOGÍA no existe o está vacío para {species}")
                continue

            if not fantasia.exists() or fantasia.stat().st_size == 0:
                print(f"[WARN] RESULTADOS FANTASIA no existe o está vacío para {species}")
                continue

            # IMPORTANTE: limpiar resultados por especie
            resultados.clear()

            # homología
            with homologia.open(encoding="utf-8") as hom:
                protes_h, gos_totales_h, id_con_go_h, id_sin_go_h, gos_por_prote_h, cobertura_h = calc_stats(hom, species, destino=0, resultados)
                calculos_h[species] = [protes_h, gos_totales_h, id_con_go_h, id_sin_go_h, gos_por_prote_h, cobertura_h]

            # FANTASIA
            with fantasia.open(encoding="utf-8") as fan:
                protes_f, gos_totales_f, id_con_go_f, id_sin_go_f, gos_por_prote_f, cobertura_f = calc_stats(fan, species, destino=1, resultados)
                calculos_f[species] = [protes_f, gos_totales_f, id_con_go_f, id_sin_go_f, gos_por_prote_f, cobertura_f]

            # calcular el solape de GO por proteína
            overlaps, total_solapados = calc_overlap_por_prote(resultados)
            solape_h = (total_solapados/gos_totales_h)*100
            solape_f = (total_solapados/gos_totales_f)*100

            # construir fila
            fila = [
                species,
                f"{protes_h} | {protes_f}",
                f"{id_con_go_h} | {id_con_go_f}",
                f"{id_sin_go_h} | {id_sin_go_f}",
                f"{cobertura_h:.3f} | {cobertura_f:.3f}",
                f"{gos_por_prote_h:.3f} | {gos_por_prote_f:.3f}",
                f"{gos_totales_h} | {gos_totales_f}",
                total_solapados,
                f"{solape_h:.3f} | {solape_f:.3f}"
            ]
            append_row(outfile, fila)

        total, gos_totales_h, gos_totales_f, total_solapados = calc_total(outfile)        
        append_row(outfile, total)
        venn = plot_venn(gos_totales_h, gos_totales_f, total_solapados)


if __name__ == "__main__":
    main()

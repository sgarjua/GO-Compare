#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from pathlib import Path
from src.parser import parse_arguments
from src.stats import calc_stats
from src.table import write_header, append_row
from src.overlap import calc_overlap_por_prote
from src.plotting import plot_venn


def main():
    args = parse_arguments()

    input_fof = Path(args.input)
    outfile = Path(args.output)

    header = [
        "Especie","Secuencias (H|F)","Con GO (H|F)","Sin GO (H|F)",
        "Cobertura% (H|F)","Media GO/sec (H|F)","GOs totales (H|F)",
        "GOs solapados","% (H|F)"
    ]
    write_header(outfile, header)

    with input_fof.open() as fof:
        for line in fof:
            if not line.strip() or line.startswith("#"): continue

            species, hom_path, fan_path = line.strip().split("\t")
            hom_path, fan_path = Path(hom_path), Path(fan_path)

            resultados = {}

            # homología
            with hom_path.open() as h:
                ph, gh, ch, sh, mph, coh = calc_stats(resultados, h, destino=0)

            # fantasia
            with fan_path.open() as f:
                pf, gf, cf, sf, mpf, cof = calc_stats(resultados, f, destino=1)

            overlaps, total_sol = calc_overlap_por_prote(resultados)
            sol_h = (total_sol / gh * 100) if gh else 0
            sol_f = (total_sol / gf * 100) if gf else 0

            row = [
                species,
                f"{ph} | {pf}",
                f"{ch} | {cf}",
                f"{sh} | {sf}",
                f"{coh:.2f} | {cof:.2f}",
                f"{mph:.2f} | {mpf:.2f}",
                f"{gh} | {gf}",
                total_sol,
                f"{sol_h:.2f} | {sol_f:.2f}"
            ]
            append_row(outfile, row)

    # diagrama final
    plot_venn(gh, gf, total_sol)


if __name__ == "__main__":
    main()

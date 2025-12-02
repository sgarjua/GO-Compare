from pathlib import Path
import csv


def write_header(outfile: Path, header):
    """Escribe cabecera sólo si el fichero no existe aún."""
    modo = "a" if outfile.exists() else "w"
    with outfile.open(modo, newline="", encoding="utf-8") as tsv:
        w = csv.writer(tsv, delimiter="\t")
        if modo == "w":
            w.writerow(header)


def append_row(outfile: Path, row):
    with outfile.open("a", newline="", encoding="utf-8") as tsv:
        w = csv.writer(tsv, delimiter="\t")
        w.writerow(row)
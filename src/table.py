from pathlib import Path
import csv

def write_header(outfile: Path, header: list):
    modo = "a" if outfile.exists() else "w"
    with outfile.open(modo, newline="", encoding="utf-8") as out:
        w = csv.writer(out, delimiter="\t")
        if modo == "w":
            w.writerow(header)

def append_row(outfile: Path, row: list):
    with outfile.open("a", newline="", encoding="utf-8") as out:
        csv.writer(out, delimiter="\t").writerow(row)

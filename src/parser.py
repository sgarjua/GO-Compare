

import argparse

def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Analiza y compara resultados GO por homología y FANTASIA."
    )

    parser.add_argument("-i", "--input",  required=True, help="Input FOF")
    parser.add_argument("-o", "--output", required=True, help="Output TSV")
    return parser.parse_args()

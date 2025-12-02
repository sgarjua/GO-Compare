
import sys
import argparse

def parse_arguments() -> argparse.Namespace:
    """Return parsed command-line arguments."""
    description = "Analiza y compara resultados de anotación GO por homología y por FANTASIA."
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument("-i", "--input",  required=True, help="Input FOF")
    parser.add_argument("-o", "--output", required=True, help="Output file name")

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()

    return parser.parse_args()

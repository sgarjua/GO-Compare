#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import sys
from src.parser import Parser

def main():
    # 1. Definir los argumentos que acepta tu herramienta
    args_def = {
        ('-i', '--input'):  {'required': True, 'help': "Archivo de entrada"},
        ('-o', '--output'): {'required': True, 'help': "Archivo de salida"},
    }

    # 2. Instanciar tu parser
    my_parser = Parser(
        description="Herramienta para análisis de anotaciones funcionales",
        args=args_def
    )

    # 3. Parsear argumentos
    args = my_parser.return_parser()

    print(args)




if __name__ == "__main__":
    main()

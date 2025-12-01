#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from typing import Dict, Tuple

class Parser:

    def __init__(self, description: str, args: Dict[tuple, Dict]):
        '''
        Descripción: un string con una descripción.
        argumentos: esto tiene su cosa; como lo haces tú es añadir primero el nombre corto del argumento, luego el largo
        y finalmente, una serie de argumentos (que pueden llegar a ser variables). Para seguir la línea que has seguido 
        y poder hacerlo genérico tienes que definir el parámetro argumentos así:

        {
            ('-i', '--input'): {'required': True, 'help':"Input FOF"}, 
            ('-o', '--output'): {'required': True, 'help':"Output file name"}
        }
        '''

        parser = argparse.ArgumentParser(description=description)
        for key , value in args.items():
            parser.add_argument(*key, **value)

        self.parser_true = parser

    def return_parser(self):
        return self.parser_true
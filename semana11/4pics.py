# !/usr/bin/env python3
import argparse, sys

DICT = '/usr/share/dict/words'
""" Esta funcion debe con las letras y el largo ver cuales del diccionario son candidatos. """
def fourpics(args):
    d = args.dictionary["A"]
    print()


parser = argparse.ArgumentParser(description='4pics - elige palabras para el juego "4 Pics and 1 word"')
parser.add_argument('-s', '--string', help='lista de letras', required=True, type=str.upper)
parser.add_argument('-l', '--length', help='largo de la palabra', type=int, required=True)
parser.add_argument('-i', '--initial', help='letra inicial de la palabra', default=None, type=str.upper)
parser.add_argument('-d', '--dictionary', help=f'archivo de diccionario ({DICT})', default=DICT, type=argparse.FileType('r'))
args = parser.parse_args()  # los argumentos quedan en args string, args length etc
print(parser)

candidates = fourpics(args)
if candidates:
    print(candidates)
    sys.exit(0)
else:
    sys.exit(1)


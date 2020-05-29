# !/usr/bin/env python3
import argparse, sys

DICT = '/usr/share/dict/words'
""" Esta funcion debe con las letras y el largo ver cuales del diccionario son candidatos. """
def fourpics(args):
    cand = []
    largo = args.length
    letraInicial = None
    listaLetras = args.string.split(',')
    print(listaLetras)
    if args.initial: 
        letraInicial = args.initial   
    while(True):
        linea = args.dictionary.readline()  # lineas del diccionario
        if not linea:
            break
        if letraInicial:
            if linea[0] == letraInicial and len(linea)-1 == largo :  #el -1 es porque la linea viene con un /n
                # resta ver que si todas las letras de la lista estan en la palabra la meta
                deberiaser = len(listaLetras)
                es = 0
                for letra in listaLetras:
                    if linea.find(letra) != -1:
                        es += 1 
                if deberiaser == es:
                    cand.append(linea)                        
        if letraInicial is None:
            if len(linea)-1 == largo:
                deberiaser = len(listaLetras)
                es = 0
                for letra in listaLetras:
                    if linea.find(letra) != -1: # es actua como contador, de la cantidad de letras que coinciden en la linea y la lista
                        es += 1 
                if deberiaser == es:
                    cand.append(linea)
    return cand

parser = argparse.ArgumentParser(description='4pics - elige palabras para el juego "4 Pics and 1 word"')
parser.add_argument('-s', '--string', help='lista de letras', required=True, type=str.upper)
parser.add_argument('-l', '--length', help='largo de la palabra', type=int, required=True)
parser.add_argument('-i', '--initial', help='letra inicial de la palabra', default=None, type=str.upper)
parser.add_argument('-d', '--dictionary', help=f'archivo de diccionario ({DICT})', default=DICT, type=argparse.FileType('r'))
args = parser.parse_args()  # los argumentos quedan en args string, args length etc
print(parser)

candidates = fourpics(args)
if candidates:
    for can in candidates:
        print(can)
    sys.exit(0)
else:
    sys.exit(1)


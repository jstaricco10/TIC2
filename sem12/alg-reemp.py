#! /usr/bin/env python3
import argparse
from collections import deque

parser = argparse.ArgumentParser(description='Toma los datos a tener en cuenta para el algoritmo de reeplazo')
# parser.add_argument('-s', '--string', help='lista de paginas', required=True, type=str.upper)
# parser.add_argument('-f', '--frames', help='frames de paginas', type=int, required=True)
# parser.add_argument('-a', '--algoritmo', help='algoritmo de reemplazo a usar', default="FIFO", type=str.upper,
#                     required=True)
parser.add_argument('-v', '--verbose', help='Paso a paso de estado de frames, si no es '' .', default='')
args = parser.parse_args()  # los argumentos quedan en args string, args length etc
print(parser)
n = 3  # este sera el argumento de args.frames
list = [None] * n
frames = deque(list)
string = "2523464"

""" El algoritmo fifo agrega, con un contador de pos, aumenta el contador y si el contador es n-1 se reinicia a 0.
Cuando llega una reemplaza en la posicion indicada en contador, si es que no esta en los frames, si esta suma
 1 al contador de fallas"""


def fifo(pages, frames):
    fin = len(frames)
    fallas = 0
    posicion = 0
    # voy agregando char en la posicion posicion de frames con insert(i,a)
    for c in pages:
        if c in frames:
            fallas += 1
        else:
            frames[posicion] = c
            posicion += 1
            if posicion == fin:
                posicion = 0
        print(frames)
        print(fallas)


fifo(string, frames)

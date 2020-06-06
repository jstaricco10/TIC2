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

frames = deque([], 4)
print(frames[1])

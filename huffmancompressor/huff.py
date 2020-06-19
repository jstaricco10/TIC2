#! /usr/bin/env python3

from heapq import heappush, heappop, heapify
from collections import defaultdict, namedtuple
import argparse
import os

# traducir huff a named tuple huff(symbol,code), named tuple no porque una tupla no permite asignacion, debe ser un dict

"""
typedef struct compr_header: # 8 bytes: cabezal de archivo comprimido
    uint16_t    magic_nbr # número mágico (2)
    uint8_t     sym_arraylen # largo del array de los Symcode (1)
    uint8_t     sym_arraysize #  tamaño de cada elemento del array anterior (1)
    uint32_t    filelen # largo del archivo original en bytes (4)
} Compr_header
"""

""" Se debe hacer una clase para el Header?"""
class Header:
    def __init__(self, magic_nbr, sym_arraylen, sym_arraysize, filelen):
        self.magic_nbr = magic_nbr
        self.sym_arraylen = sym_arraylen
        self.sym_arraysize = sym_arraysize
        self.filelen = filelen


def encode(symb2freq):
    """Huffman encode the given dict mapping symbols to weights"""
    huffCode = namedtuple('huffCode', ' symbol code')
    lista = []
    print(symb2freq)
    heap = [[wt, [sym, ""]] for sym, wt in symb2freq.items()]
    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    # debemos hacer esto con el pop del heap salteando el primero, hay que optimizar esto
    salteodelprimero = 0
    for elem in heappop(heap):
        if salteodelprimero == 0:
            salteodelprimero += 1
        else:
            pop = elem
            lista.append(huffCode(pop[0], pop[1]))
    # ordeno por codigo??, con item y atr getter de la letra
    return lista


""" Comprimimos el archivo en uno nuevo con .huf"""


def compress(huff, args):
    file = open(args.file, 'rb')
    # print(huff)
    newfile = open(args.file + ".huff", 'wb')
    # primero debemos hacer el cabezal
    numeromagico = "DG"
    sym_arraylen = len(huff)
    sym_arraysize = len(huff[1])
    filelen = os.stat(args.file).st_size

    # luego recorrer el file y poner en el nuevo archivo la coficacion al byte que le corresponda
    codificadoTotal = ""
    while True:
        b = file.read(1)
        if not b:
            break
        for h in huff:
            if b == h.symbol:
                codificado = h.code
                codificadoTotal += codificado
    # debemos agregar en cod total los 0 al final que falten para tener tamano multiplo de 8
    cantAAgregar = 8 - (len(codificadoTotal) % 8)
    for _ in range(cantAAgregar):
        codificadoTotal += '0'
    if len(codificadoTotal)/8 > filelen and not args.force:
        file.close()
        return
    newfile.write(bytearray(int(codificadoTotal[x:x + 8], 2) for x in range(0, len(codificadoTotal), 8)))
    # analizar, splitea el string en "8 char
    # chunks https://stackoverflow.com/questions/7290943/write-a-string-of-1s-and-0s-to-a-binary-file
    newfile.close()
    file.close()
    return


def main():
    parser = argparse.ArgumentParser(description='Parsea los datos pasados en consola')
    parser.add_argument('file', help='Archivo a comprimir')
    parser.add_argument('-f', '--force', help='Fuerza compresion aunque aumente el tamano', type=str.upper)
    parser.add_argument('-v', '--verbose', help='Imprime informacion del avance del proceso', action='store_true')
    # con el parser debo procesar el nombre del archivo
    args = parser.parse_args()
    file = open(args.file, 'rb')  # debemos controlar el caso de que el file no sea encontrado
    symb2freq = defaultdict(int)
    while True:
        b = file.read(1)
        if not b:
            break
        symb2freq[b] += 1
    huff = encode(symb2freq)
    file.close()
    if args.verbose:
        print("Symbol\tWeight\tHuffman Code")
        for p in huff:
            print("%s\t%s\t%s" % (p.symbol, symb2freq[p.symbol], p.code))
    # print(huff)
    compress(huff, args)


if __name__ == '__main__':
    main()

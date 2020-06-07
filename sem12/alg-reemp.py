#! /usr/bin/env python3
import argparse
from collections import deque

""" El algoritmo fifo agrega, con un contador de pos, aumenta el contador y si el contador es n-1 se reinicia a 0.
Cuando llega una reemplaza en la posicion indicada en contador, si es que no esta en los frames, si esta suma
 1 al contador de fallas"""


def fifo(pages, frames, v):
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
        if v:
            print(frames)
            print(fallas)
    print("El resulatado es: ")
    print(frames)
    print(fallas)


"""El algoritmo optimo reemplaza la pagina que no va a ser usada por en mayor tiempo posible """


def determinarposicionOpt(frames, pages, posicionc, fin):
    aux = frames.copy()
    # posicionc += 1
    termino = len(aux)
    print(frames)
    print(aux)
    while termino != 1:
        for c in frames:
            if pages[posicionc] in frames:
                aux.remove(c)
                termino -= 1
            posicionc += 1
            if posicionc == len(pages):
                posicionc = 0
    return frames.index(aux[0])


# TODO a retocar
def optimal(pages, frames, v):
    fallas = 0
    posicion = 0
    posicionc = 0
    fin = len(frames)
    for c in pages:
        if c in frames:
            fallas += 1
        else:
            if None in frames:
                frames[posicion] = c
                posicion += 1
            else:
                posicion = determinarposicionOpt(frames, pages, posicionc, fin)
                print("La posicion a reemplazar es " + str(posicion))
                frames[posicion] = c
        posicionc += 1
        if v:
            print(frames)
            print(fallas)
    print("El resulatado es: ")
    print(frames)
    print(fallas)


""" En el lru se elige para reemplazar la que fue accedida hace mas tiempo y esa se reemplaza. Puedo
reemplazar siempre por la posicion 0 y hacer rotar mi dequeue len(frames)-1 veces"""


def lru(pages, frames, v):
    fallas = 0
    posicion = 0
    rotaciones = len(frames) - 1
    for c in pages:
        if c in frames:
            fallas += 1
        else:
            if None in frames:
                frames[posicion] = c
                posicion += 1
            else:
                frames[0] = c
                frames.rotate(rotaciones)
        if v:
            print(frames)
            print(fallas)
    print("El resulatado es: ")
    print(frames)
    print(fallas)


def main():
    parser = argparse.ArgumentParser(description='Toma los datos a tener en cuenta para el algoritmo de reeplazo')
    parser.add_argument('-s', '--string', help='lista de paginas', required=True, type=str.upper)
    parser.add_argument('-f', '--frames', help='frames de paginas', type=int, required=True)
    parser.add_argument('-a', '--algorithm', help='algoritmo de reemplazo a usar', default="fifo", type=str.upper,
                        required=True)
    parser.add_argument('-v', '--verbose', help='Paso a paso de estado de frames si se pone', default='')
    args = parser.parse_args()  # los argumentos quedan en args string, args length etc
    list = [None] * int(args.frames)
    frames = deque(list)
    string = args.string

    if args.algorithm == "LRU":
        lru(string, frames, args.verbose)
    elif args.algorithm == "OPTIMAL":
        optimal(string, frames, args.verbose)
    elif args.algorithm == "FIFO":
        fifo(string, frames, args.verbose)
    else:
        print("Escoja un algoritmo a ejecutar entre lru, optimal y fifo.")


if __name__ == '__main__':
    main()

#! /usr/bin/env python3
import argparse
import sys
import random
from collections import namedtuple


def verifciacion(jug1):
    res = ''
    nums = ''
    ocho = 0
    nueve = 0
    diez = 0
    jota = 0
    q = 0
    k = 0
    ases = 0
    # solo hay 3 tipos de escalera
    esQ = False
    esK = False
    esA = False
    negras = 0
    rojas = 0
    for elem in jug1:
        nums = nums + elem.numero
        if elem.numero == '8':
            ocho += 1
        elif elem.numero == '9':
            nueve += 1
        elif elem.numero == '10':
            diez += 1
        elif elem.numero == 'J':
            jota += 1
        elif elem.numero == 'Q':
            q += 1
        elif elem.numero == 'K':
            k += 1
        else:
            ases += 1
        if elem.palo == 'C' or elem.palo == 'D':
            rojas = + 1
        else:
            negras = +1
    if sorted(nums) == sorted('8910JQ'):
        esQ = True
    elif sorted(nums) == sorted('910JQK'):
        esK = True
    elif sorted(nums) == sorted('10JQKA'):
        esA = True
    # Ahora procedemos a buscar la combinacion mas alta y retornarla
    # Vamos en sentido descendente chqueando cada una
    # ESCALERA REAL
    if esA and (negras == 4 or rojas == 4):
        return "Escalera Real"
    # ESCALERA COLOR
    if (esK or esQ) and (rojas == 4 or negras == 4):
        return "Escalera Color"
    # POKER
    if ases == 4:
        return "Poker de ases"
    if k == 4:
        return "Poker de K"
    if q == 4:
        return "Poker de Q"
    if jota == 4:
        return "Poker de j"
    if diez == 4:
        return "Poker de 10"
    if nueve == 4:
        return "Poker de 9"
    if ocho == 4:
        return "Poker de 8"
    # FULL
    if (ases == 3 or k == 3 or q == 3 or jota == 3 or diez == 3 or nueve == 3 or ocho == 3) and (
            ases == 2 or k == 2 or q == 2 or jota == 2 or diez == 2 or nueve == 2 or ocho == 2):
        return "Full"
    # COLOR
    if negras == 4 or rojas == 4:
        return "Color"
    # ESCALERAS
    if esA:
        return "Escalera en A"
    if esK:
        return "Escalera en K"
    if esQ:
        return "Escalera en Q"
    # PIERNAS
    if ases == 3:
        return "Pierna en A"
    if k == 3:
        return "Pierna en K"
    if q == 3:
        return "Pierna en Q"
    if jota == 3:
        return "Pierna en J"
    if diez == 3:
        return "Pierna en 10"
    if nueve == 3:
        return "Pierna en 9"
    if ocho == 3:
        return "Pierna en 8"
    # DOBLE PARES
    if ases == 2:
        if k == 2:
            return "Par de As y Ks"
        if q == 2:
            return "Par de As y Ks"
        if jota == 2:
            return "Par de As y Qs"
        if diez == 2:
            return "Par de As y 10s"
        if nueve == 2:
            return "Par de As y 9s"
        if ocho == 2:
            return "Par de As y 8s"
    if k == 2:
        if q == 2:
            return "Par de Ks y Qs"
        if jota == 2:
            return "Par de Ks y Js"
        if diez == 2:
            return "Par de Ks y 10s"
        if nueve == 2:
            return "Par de Ks y 9s"
        if ocho == 2:
            return "Par de Ks y 8s"
    if q == 2:
        if jota == 2:
            return "Par de Qs y Js"
        if diez == 2:
            return "Par de Qs y 10s"
        if nueve == 2:
            return "Par de Qs y 9s"
        if ocho == 2:
            return "Par de Qs y 8s"
    if jota == 2:
        if diez == 2:
            return "Par de Js y 10s"
        if nueve == 2:
            return "Par de Js y 9s"
        if ocho == 2:
            return "Par de Js y 8s"
    if diez == 2:
        if nueve == 2:
            return "Par de 10s y 9s"
        if ocho == 2:
            return "Par de 10s y 8s"
    if nueve == 2:
        if ocho == 2:
            return "Par de 9s y 8s"
    # PARES
    if ases == 2:
        return "Par de As"
    if k == 2:
        return "Par de Ks"
    if q == 2:
        return "Par de Qs"
    if jota == 2:
        return "Par de Js"
    if diez == 2:
        return "Par de 10s"
    if nueve == 2:
        return "Par de 9s"
    if ocho == 2:
        return "Par de 8s"


def main():
    carta = namedtuple('carta', 'numero palo')
    mazo = [carta('8', 'P'), carta('9', 'P'), carta('10', 'P'), carta('J', 'P'), carta('Q', 'P'), carta('K', 'P'),
            carta('A', 'P'),
            carta('8', 'C'), carta('9', 'C'), carta('10', 'C'), carta('J', 'C'), carta('Q', 'C'), carta('K', 'C'),
            carta('A', 'C'),
            carta('8', 'D'), carta('9', 'D'), carta('10', 'P'), carta('J', 'D'), carta('Q', 'D'), carta('K', 'D'),
            carta('A', 'D'),
            carta('8', 'T'), carta('9', 'T'), carta('10', 'P'), carta('J', 'T'), carta('Q', 'T'), carta('K', 'T'),
            carta('A', 'T')]
    random.shuffle(mazo)
    jug1 = []
    jug2 = []
    jug3 = []
    jug4 = []
    jug5 = []
    for _ in range(5):
        jug1.append(mazo.pop())
        jug2.append(mazo.pop())
        jug3.append(mazo.pop())
        jug4.append(mazo.pop())
        jug5.append(mazo.pop())
    l = []
    ver = ''
    for elem in jug1:
        s = elem.numero + elem.palo
        l.append(s)
    ver = verifciacion(jug1)
    if ver != None:
        print(str(l) + '  ' + ver)
    else:
        print(l)
    l.clear()
    for elem in jug2:
        s = elem.numero + elem.palo
        l.append(s)
    ver = verifciacion(jug2)
    if ver != None:
        print(str(l) + '  ' + ver)
    else:
        print(l)
    l.clear()
    for elem in jug3:
        s = elem.numero + elem.palo
        l.append(s)
    ver = verifciacion(jug3)
    if ver != None:
        print(str(l) + '  ' + ver)
    else:
        print(l)
    l.clear()
    for elem in jug4:
        s = elem.numero + elem.palo
        l.append(s)
    ver = verifciacion(jug4)
    if ver != None:
        print(str(l) + '  ' + ver)
    else:
        print(l)
    l.clear()
    for elem in jug5:
        s = elem.numero + elem.palo
        l.append(s)
    ver = verifciacion(jug5)
    if ver != None:
        print(str(l) + '  ' + ver)
    else:
        print(l)
    l.clear()
    pass


if __name__ == '__main__':
    main()
    sys.exit(0)

# !/usr/bin/env python3
# truco.py

import random

mazo = [('1', 'Oro'), ('2', 'Oro'), ('3', 'Oro'), ('4', 'Oro'), ('5', 'Oro'), ('6', 'Oro'), ('7', 'Oro'), ('10', 'Oro'),
        ('11', 'Oro'), ('12', 'Oro'),
        ('1', 'Basto'), ('2', 'Basto'), ('3', 'Basto'), ('4', 'Basto'), ('5', 'Basto'), ('6', 'Basto'), ('7', 'Basto'),
        ('10', 'Basto'), ('11', 'Basto'), ('12', 'Basto'),
        ('1', 'Espada'), ('2', 'Espada'), ('3', 'Espada'), ('4', 'Espada'), ('5', 'Espada'), ('6', 'Espada'),
        ('7', 'Espada'), ('10', 'Espada'), ('11', 'Espada'), ('12', 'Espada'),
        ('1', 'Copa'), ('2', 'Copa'), ('3', 'Copa'), ('4', 'Copa'), ('5', 'Copa'), ('6', 'Copa'), ('7', 'Copa'),
        ('10', 'Copa'), ('11', 'Copa'), ('12', 'Copa')]

muestra = None
jug1 = []
jug2 = []
florjug1 = None
florjug2 = None

dicPiezas = {'2': 30, '4': 29, '5': 28, '11': 27, '10': 27}
dicNoPiezas = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '10': 0, '11': 0, '12': 0}

""" Hay flor si: 
    - 3 del mismo palo
    - 2 piezas ,3 piezas
    - 1 pieza y dos del mismo palo"""


def flor(jug, muestra):
    noPiezas = []
    paloMuestra = muestra[1]
    nropiezas = 0
    for carta in jug:
        if carta[1] == paloMuestra:
            if carta[0] == '2' or carta[0] == '4' or carta[0] == '5' or carta[0] == '11' or carta[0] == '10':
                nropiezas += 1
            else:
                noPiezas.append(carta)
        else:
            noPiezas.append(carta)
    if nropiezas > 1:
        return 0
    if nropiezas == 1:
        if noPiezas[0][1] == noPiezas[1][1]:
            return 0
    return 1

""" El envido son las dos mas altas con valores de piezas o si no hay pizas y hay dos del mismo palo son esas, mas 20
el 10, 11 y 12 son 0"""
def calculoEnvido(jug, muestra):
    envido = 0
    paloMuestra = muestra[1]
    for carta in jug: #sacamos el valor de la pieza del diccionario si hay pieza
        if carta[1] == paloMuestra:
            if carta[0] == '2':
                envido +=30
    return envido


def partida():
    random.shuffle(mazo)
    for i in range(0, 3):
        jug1.append(mazo.pop())
        jug2.append(mazo.pop())
    print(jug1)
    print(jug2)
    muestra = mazo.pop()
    print("La muestra es " + str(muestra))
    if flor(jug1, muestra) == 0:
        print("El jugador 1 tiene flor")
    else:
        print("El jugador 1 tiene ENVIDO de " + str(calculoEnvido(jug1, muestra)) + " puntos")
    if flor(jug2, muestra) == 0:
        print("El jugador 2 tiene flor")
    else:
        print("El jugador 2 tiene ENVIDO de " + str(calculoEnvido(jug2, muestra)) + " puntos")


partida()

# !/usr/bin/env python3
# truco.py

import random

mazo = [('1', 'Oro'), ('2', 'Oro'), ('3', 'Oro'), ('4', 'Oro'), ('5', 'Oro'), ('6', 'Oro'), ('7', 'Oro'), ('10', 'Oro'), ('11', 'Oro'), ('12', 'Oro'),
('1', 'Basto'), ('2', 'Basto'), ('3', 'Basto'), ('4', 'Basto'), ('5', 'Basto'), ('6', 'Basto'), ('7', 'Basto'), ('10', 'Basto'), ('11', 'Basto'), ('12', 'Basto'),
('1', 'Espada'), ('2', 'Espada'), ('3', 'Espada'), ('4', 'Espada'), ('5', 'Espada'), ('6', 'Espada'), ('7', 'Espada'), ('10', 'Espada'), ('11', 'Espada'), ('12', 'Espada'),
('1', 'Copa'), ('2', 'Copa'), ('3', 'Copa'), ('4', 'Copa'), ('5', 'Copa'), ('6', 'Copa'), ('7', 'Copa'), ('10', 'Copa'), ('11', 'Copa'), ('12', 'Copa')]

muestra = None
jug1 = []
jug2 = []
florjug1 = None
florjug2 = None

def partida():
    # global florjug1,florjug2,muestra
    random.shuffle(mazo)
    for i in range (0,3):
        jug1.append(mazo.pop())
        jug2.append(mazo.pop())
    print(jug1)
    print(jug2)
    muestra = mazo.pop()
    print("La muestra es " + str(muestra)
    if  flor(jug1,muestra) == 0:
        print("El jugador 1 tiene flor")
    else:
        print("El jugador 1 tiene ENVIDO de " + calculoEnvido(jug1, muestra) + "puntos")    
    if flor(jug2, muestra) == 0 :
        print("El jugador 2 tiene flor")
    else:
        print("El jugador 2 tiene ENVIDO de " + calculoEnvido(jug2, muestra) + "puntos")            

def flor(jug, muestra):
    return 0


def calculoEnvido(jug, muestra):
    return 0   

partida()
# ej4.py
"""4. Modelar un juego de dominó. Las 28 fichas se “mezclarán” (módulo random, función random.shuffle) y
formarán el “pozo”. Dos jugadores toman cada uno 8 fichas del pozo y estarán en su “mano”.
El objetivo del juego es “bajar” las fichas de la “mano” a la “mesa”.
Comienza el jugador que puede bajar el doble 6, si ninguno lo tiene, el doble 5, etc.
Si ninguno tiene un doble comienza el que tiene la ficha de mayor valor, considerando el número más alto y
luego el más bajo de esa ficha ( por ej. 62 le gana a 54). A partir de ese momento, el otro jugador deberá
poner una ficha y así sucesivamente se van alternando. La regla básica del dominó es que la ficha a poner debe
tener uno de sus números iguales a cualquier extremo de las fichas de la “mesa”. Si el jugador no tiene una ficha
que cumpla la regla, debe robar del pozo hasta que la tenga o hasta que el pozo quede vacío.
Gana el jugador que se quede sin fichas. En caso de que ninguno de los jugadores pueda bajar todas sus fichas,
gana el que tenga menos fichas en la mano."""

import random

unoseis = [6, 5, 4, 3, 2, 1, 0]

mazo = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6),
        (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
        (2, 2), (2, 3), (2, 4), (2, 5), (2, 6),
        (3, 3), (3, 4), (3, 5), (3, 6),
        (4, 4), (4, 5), (4, 6),
        (5, 5), (5, 6),
        (6, 6)]
# print(mazo)
pozo = []
jug1 = []
jug2 = []
indexes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
           15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
empezo = 0  # para ver quien tiro primero, y asi seguir los turnos
extremoizq = 0
extremoder = 0
# queda actulizar quien va y seguir hasta que uno se quede sin cartas o el mazo se acabe y ver quien gano


def partida():
    global empezo, extremoizq, extremoder
    random.shuffle(mazo)
    # print(mazo)
    for i in range(0, 7):
        jug1.append(mazo.pop())
        jug2.append(mazo.pop())
    print(jug1)
    print(jug2)

    primermovimiento(jug1, jug2)
    if len(jug1) > len(jug2):
        empezo = 2
        print("va el 1")
    elif len(jug1) < len(jug2):
        empezo = 1
        print("va el 2")
    # se deben  hacer movimientos mientas haya en el mazo, o los jugadores tengan cartas
    while len(jug1) > 0 and len(jug2) > 0 and len(mazo) > 0:
        movimiento(jug1, jug2)
    print("Los resultados finales fueron: ")
    print("El jugador 1 termino con " + str(len(jug1)) + " fichas")
    print("El jugador 2 termino con " + str(len(jug2)) + " fichas")
    print("El mazo termino con " + str(len(mazo)) + " fichas")
    print(pozo)
    if len(jug1) > len(jug2):
        print("Gano el jugador 2!")
    elif len(jug1) < len(jug2):
        print("Gano el jugador 1!")
    else:
        print("Hubo empate!")

# falta contemplar el caso en que niguno tiene un doble
def primermovimiento(jug1, jug2):
    global extremoizq, extremoder
    for i in unoseis:
        if (i, i) in jug1:
            jug1.remove((i, i))
            pozo.append((i, i))
            extremoizq = i
            extremoder = i
            print(pozo)
            break
        if (i, i) in jug2:
            jug2.remove((i, i))
            pozo.append((i, i))
            extremoizq = i
            extremoder = i
            print(pozo)
            break


def movimiento(jug1, jug2):
    global empezo, extremoizq, extremoder
    if empezo == 2:
        print("jugada del 1")
        for elem in jug1:
            # hay que ver si una ficha del jugador encaja en uno de los extremos del pozo e insertarla, si no se saca una del mazo hasta que pueda
            if elem[0] == extremoizq:
                jug1.remove(elem)
                pozo.insert(0, elem)  # falta ponerle que es en la posicion 0
                extremoizq = elem[1]
                empezo = 1  # va el 2 ahora
                break
                # el elemento de jug1 se inserta por la izq y se cambia extremo izq por elem [1]
            elif elem[0] == extremoder:
                jug1.remove(elem)
                pozo.append(elem)  # falta ponerle que es en la posicion ultima
                extremoder = elem[1]
                empezo = 1  # va el 2 ahora
                break
                # el elemento de jug1 se inserta por la der y se cambia extremo izq por elem [1]
            elif elem[1] == extremoizq:
                jug1.remove(elem)
                pozo.insert(0, elem)  # falta ponerle que es en la posicion 0
                extremoizq = elem[0]
                empezo = 1  # va el 2 ahora
                break
                # el elemento de jug1 se inserta por la izq y se cambia extremo izq por elem [0]
            elif elem[1] == extremoder:
                jug1.remove(elem)
                pozo.append(elem)  # falta ponerle que es en la posicion ultima
                extremoder = elem[0]
                empezo = 1  # va el 2 ahora
                break
                # el elemento de jug1 se inserta por la der y se cambia extremo izq por elem [1]
        jug1.append(mazo.pop())
        empezo = 1

    elif empezo == 1:
        print("jugada del 2")
        for elem in jug2:
            # hay que ver si una ficha del jugador encaja en uno de los extremos del pozo e insertarla, si no se saca una del mazo hasta que pueda
            if elem[0] == extremoizq:
                jug2.remove(elem)
                pozo.insert(0, elem)  # falta ponerle que es en la posicion 0
                extremoizq = elem[1]
                empezo = 2  # va el 1 ahora
                break
                # el elemento de jug2 se inserta por la izq y se cambia extremo izq por elem [1]
            elif elem[0] == extremoder:
                jug2.remove(elem)
                pozo.append(elem)  # falta ponerle que es en la posicion ultima
                extremoder = elem[1]
                empezo = 2  # va el 1 ahora
                break
                # el elemento de jug2 se inserta por la der y se cambia extremo izq por elem [1]
            elif elem[1] == extremoizq:
                jug2.remove(elem)
                pozo.insert(0, elem)  # falta ponerle que es en la posicion 0
                extremoizq = elem[0]
                empezo = 2  # va el 1 ahora
                break
                # el elemento de jug2 se inserta por la izq y se cambia extremo izq por elem [0]
            elif elem[1] == extremoder:
                jug2.remove(elem)
                pozo.append(elem)  # falta ponerle que es en la posicion ultima
                extremoder = elem[0]
                empezo = 2  # va el 1 ahora
                break
        jug2.append(mazo.pop())
        empezo = 2
                # el elemento de jug2 se inserta por la der y se cambia extremo izq por elem [1]
    # print(pozo)


partida()

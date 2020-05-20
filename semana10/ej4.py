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

mazo = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6),
        (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
        (2, 2), (2, 3), (2, 4), (2, 5), (2, 6),
        (3, 3), (3, 4), (3, 5), (3, 6),
        (4, 4), (4, 5), (4, 6),
        (5, 5), (5, 6),
        (6, 6)]
# print(mazo)
jug1 = []
jug2 = []
indexes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
           15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
indexes = random.shuffle(indexes)
print(indexes)




"""" 2 La función inversa a la anterior. Escribir la función de_romano(rom) que recibe como argumento
un string en notación romana y retorna su valor entero. No preocuparse por la corrección de la notación romana,
pero detectar la mayor cantidad de errores posibles en la entrada. """

"""I - 1  , V - 5  X - 10 ,  L - 50, C - 100, D -500,  M-1000  , debemos agregar el 4,9, 40,90,400,900"""

dic = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50, "XC": 90, "C": 100, "CD": 400, "D": 500,
       "CM": 900, "M": 1000}
# XCII : 92
# veo un numero, es mas grande que el siguiente lo guardo en anterior y se sigue, si es mas chico lo resto dos veces


def de_romano(rom):
    numero_ant = 0
    result = 0
    arr = [char for char in rom]
    cont = 0
    for i in arr:
        if cont == 0:
            cont += 1
            numero_ant = dic[i]
        result += dic[i]
        if dic[i] > numero_ant:
            result -= 2 * numero_ant
            numero_ant = dic[i]
        else:
            numero_ant = dic[i]
    return result


print(de_romano("XCII"))

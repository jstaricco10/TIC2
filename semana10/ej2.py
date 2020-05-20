"""" 2 La función inversa a la anterior. Escribir la función de_romano(rom) que recibe como argumento
un string en notación romana y retorna su valor entero. No preocuparse por la corrección de la notación romana,
pero detectar la mayor cantidad de errores posibles en la entrada. """

"""I - 1  , V - 5  X - 10 ,  L - 50, C - 100, D -500,  M-1000  """


def de_romano(rom):
    result = 0
    arr = [char for char in rom]
    for i in arr:
        if i == 'I':
            result = result + 1
        elif i == 'V':
            result = result + 5
        elif i == 'X':
            result = result + 10
        elif i == 'L':
            result = result + 50
        elif i == 'C':
            result = result + 100
        elif i == 'D':
            result = result + 500
        elif i == 'M':
            result = result + 1000
        else:
            return print("NUMERO INVALIDO")


    return result

# una buena forma de manejar la entrada podria ser un contador que no pase de 3 numeros romanos iguales ya que en ese
# caso el numero romano en input seria invalido

print(de_romano(""))

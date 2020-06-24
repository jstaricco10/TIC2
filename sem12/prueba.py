#! /usr/bin/env python3

""" sets (conjuntos): Un conjunto, es una colección no ordenada y sin elementos repetidos.
Los usos básicos de éstos incluyen verificación de pertenencia y eliminación de entradas duplicadas."""


def main():
    set1 = {4.0, 'Carro', True}
    print(set1)  # El orden se imprime al azar
    # for e in set1:
    #     print(e)
    set1.discard(True)
    print(set1)
    dic = {1: "uno", 2: "dos"}
    set1.update(dic)
    print(set1)
    lista = [1, 3.1416, 'j', 'jarroba.com', True]
    min = ['a', 'b', 'c']
    x = [i for i in range(10)]
    print(x)
    comprLis = [item.upper() for item in min]
    print(comprLis)
    num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
    print(num_list)
    dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    # Double each value in the dictionary
    double_dict1 = {k: v * 2 for (k, v) in dict1.items()}
    print(double_dict1)
    new_dict_comp = {n: n ** 2 for n in range(10) if n % 2 == 0}
    # diccionario con key divisible por 2 en range 10 y con valor el cuadrado del numero
    print(new_dict_comp)


if __name__ == '__main__':
    main()

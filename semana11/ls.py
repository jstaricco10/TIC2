#! /usr/bin/env python3

# Modulos sugeridos  os, stat, pwd, grp, datetime, sys
import argparse
import datetime, os, stat, pwd, grp, sys

from collections import namedtuple

""" -a incluye los archivos cuyo nombre comienza con punto
• -d lista el propio directorio, no los archivos contenidos en él
• -i muestra en la primera columna el número de nodo-i
• -l genera un listado largo
• -t ordena según fecha de modificación en lugar de alfabético
• La lista de nombres puede incluir archivos o directorios. Por defecto si el nombre es un
directorio muestra un cabezal con el directorio seguido de dos puntos, luego los
archivos contenidos en él.
Este ejercicio es largo para dejarlo completo. Se sugiere ir agregando la funcionalidad de las banderas una a una,
 en este orden: -l, -a, -i, -d, -t. 
"""


def convert_date(timestamp):
    d = datetime.datetime.fromtimestamp(timestamp)
    formated_date = d.strftime('%d %b %Y')
    return formated_date


def main():
    parser = argparse.ArgumentParser(description='Parsea los datos pasados en consola')
    parser.add_argument('-l', help='genera un listado largo', action='store_true')
    parser.add_argument('-a', '--all', help='incluye los archivos cuyo nombre comienza con punto', action='store_true')
    parser.add_argument('-i', '--inode', help='muestra en la primera columna el número de nodo-i', action='store_true')
    parser.add_argument('-d', '--directory', help='lista el propio directorio, no los archivos contenidos en él',
                        action='store_true')
    parser.add_argument('-t', help='ordena según fecha de modificación en lugar de alfabético',
                        action='store_true')
    # parser.add_argument('nombre', help='Nombres de archivos o directorios')

    # con el parser debo procesar el nombre del archivo
    args = parser.parse_args()
    dir = os.scandir(os.getcwd())
    # for file in dir:
    #     if not args.all:
    #         if file.name[0] != '.':
    #             print(file.name)
    #     else:
    #         print(file.name)
    # if args.i:
    #     print(file.name ) for file in dir
    if args.l:
        for file in dir:
            print(convert_date(file.stat().st_mtime) + ' - ' + file.name + ' - ' + str(file.stat().st_size) + ' bytes')
    pass


if __name__ == '__main__':
    main()

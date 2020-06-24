#! /usr/bin/env python3
import argparse
import sys
import os
from collections import namedtuple


def main():
    parser = argparse.ArgumentParser(description='Parsea los datos del archivo pasado en consola')
    parser.add_argument('dir', help='directorio al cual le analizamos los inode, se debe pasar path relativo')
    args = parser.parse_args()
    path = args.dir

    fileTuple = namedtuple('fileTuple', 'name inode')
    dir = os.scandir(path)
    print(path)
    list = []
    links = {}
    for elem in dir:
        print(elem.name, " :", os.stat(elem.name).st_ino)
        list.append(fileTuple(elem.name, os.stat(elem.name).st_ino))
    # Restaria ver cuales son links y ponerlos en pantalla con el inode al que apuntan
    for e in list:
        links[e.inode] = []
    for e in list:
        links[e.inode].append(e.name)
    print("Los inodes presentes con sus respectivos files son:")
    for e in links:
        print(e)
        print(links[e])
        print()
    pass


if __name__ == '__main__':
    main()
    sys.exit(0)
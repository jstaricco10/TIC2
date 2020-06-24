#! /usr/bin/env python3
import argparse
import sys
import os


def main():
    parser = argparse.ArgumentParser(description='Parsea los datos del archivo pasado en consola')
    parser.add_argument('dir', help='directorio al cual le analizamos los inode')
    args = parser.parse_args()
    path = args.dir

    dir = os.scandir(path)
    print(path)
    for elem in dir:
        print(elem.name, " :", elem.inode())
    pass


if __name__ == '__main__':
    main()
    sys.exit(0)
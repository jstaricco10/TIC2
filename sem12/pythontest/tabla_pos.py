#! /usr/bin/env python3
import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description='Parsea los datos del archivo pasado en consola')
    parser.add_argument('file', help='Archivo json con resultados')
    args = parser.parse_args()
    file = open(args.file, 'r')



if __name__ == '__main__':
    main()
    sys.exit(0)
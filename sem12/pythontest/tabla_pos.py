#! /usr/bin/env python3
import argparse
import json
import sys
from collections import namedtuple


def main():
    parser = argparse.ArgumentParser(description='Parsea los datos del archivo pasado en consola')
    parser.add_argument('file', help='Archivo json con resultados')
    args = parser.parse_args()
    file = json.load(open(args.file))  # a este punto tenemos un diccionario con serie equipos y partidos
    # print(file)
    resultadosTotales = {}
    for serie in file:
        equipos = file[serie]['Equipos']
        # resultadosequipo = namedtuple('resultadoequipo', 'eq jug gan em per dg gf gc pts')
        resultados = []
        for eq in equipos:
            resultados.append({'Equipo': eq, 'jug': 0, 'gan': 0, 'em': 0, 'per': 0, 'dg': 0, 'gf': 0,
                               'gc': 0, 'pts': 0})
        partidos = file[serie]['Partidos']
        # Al final hacemos un append a resultados totales con key serie y valor resultados en cada paso del for
        # Es decir para todas las series
        # print(partidos)
        goles1 = 0
        goles2 = 0
        eq1 = ''
        eq2 = ''
        for par in partidos:
            for elem in par:
                if eq1 == '':
                    eq1 = elem
                    goles1 = par[elem]
                else:
                    eq2 = elem
                    goles2 = par[elem]
                for res in resultados:
                    if res['Equipo'] == eq1:
                        res['jug'] += 1
                        res['dg'] += goles1
                        res['dg'] -= goles2
                        res['gf'] += goles1
                        res['gc'] -= goles2
                    if res['Equipo'] == eq2:
                        res['jug'] += 1
                        res['dg'] += goles2
                        res['dg'] -= goles1
                        res['gf'] += goles2
                        res['gc'] -= goles1
                    if goles1 > goles2:
                        if res['Equipo'] == eq1:
                            res['gan'] += 1
                            res['pts'] += 3
                        if res['Equipo'] == eq2:
                            res['per'] += 1
                    elif goles1 == goles2:
                        if res['Equipo'] == eq1:
                            res['em'] += 1
                            res['pts'] += 1
                        if res['Equipo'] == eq2:
                            res['em'] += 1
                            res['pts'] += 1
                    else:
                        if res['Equipo'] == eq1:
                            res['per'] += 1
                        if res['Equipo'] == eq2:
                            res['gan'] += 1
                            res['pts'] += 3
                goles1 = 0
                goles2 = 0
                eq1 = ''
                eq2 = ''
        resultadosTotales[serie] = resultados
        # print(partidos)
    print(resultadosTotales)
    Linea = namedtuple('Linea', 'eq jug gan emp per dg gf gc pts')
    linefmt = '{eq:12} {jug:3} {gan:3} {emp:3} {per:3} {dg:3} {gf:3} {gc:3} {pts:3}'
    header = Linea(eq='Equipo', jug='Jug', gan='Gan', emp='Emp', per='Per',
                   dg='DG', gf='GF', gc='GC', pts='Pts')
    print(linefmt.format(**header._asdict()))
    # Resta armar las named tuples e ir imprimiendolas
    for serie in resultadosTotales:
        eq = resultadosTotales[serie]
        for i in range(4):
            eqDeGrupo = eq[i]
            linea = Linea(eqDeGrupo['Equipo'], eqDeGrupo['jug'], eqDeGrupo['gan'], eqDeGrupo['em'],
                          eqDeGrupo['per'], eqDeGrupo['dg'], eqDeGrupo['gf'], eqDeGrupo['gc'], eqDeGrupo['pts'])
            print(linefmt.format(**linea._asdict()))
        print()  # salto de linea entre grupos


if __name__ == '__main__':
    main()
    sys.exit(0)

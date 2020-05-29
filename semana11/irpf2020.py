# !/usr/bin/env python3
# irpf2020.py

# tabla = [3][3]
# print(tabla)


def main():
    ListasAlumnos = [[0, 31633, '0%'], [31633, 45190, '10%'],
                    [45190, 67785,'15%'], [67785,135570,'24%'],
                    [135570,225950,'25%'], [225950,338925,'27%'],
                    [338925, 519684, '31%'],[519685, '>', '36%']]
    Tabla = """\
+------------------------+
| Desde$  Hasta$   Tasa  |
|------------------------|
{}
+------------------------+\
    """
    Tabla = (Tabla.format('\n'.join("| {:<8} {:<7} {:<4}  |".format(*fila)
    for fila in ListasAlumnos)))
    print (Tabla)

if __name__=='__main__':
    main()

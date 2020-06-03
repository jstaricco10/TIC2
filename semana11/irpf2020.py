#! /usr/bin/env python3
# irpf2020.py

ListasAlumnos = [[0, 31633, '0%'], [31633, 45190, '10%'],
                [45190, 67785,'15%'], [67785,135570,'24%'],
                [135570,225950,'25%'], [225950,338925,'27%'],
                [338925, 519684, '31%'],[519685, 9999999, '36%']]

def calculo_irpf(tabla, salario):
    for elemento in tabla:
        if elemento[0] < salario< elemento[1]:
            print(elemento[2])
            if elemento[2] == '0%':
                return int(salario*0)
            elif elemento[2] == '10%':
                return int(salario*0.1)
            elif elemento[2] == '15%':
                return int(salario*0.15)           
            elif elemento[2] == '24%':
                return int(salario*0.24)
            elif elemento[2] == '25%':
                return int(salario*0.25)  
            elif elemento[2] == '27%':
                return int(salario*0.27)          
            elif elemento[2] == '31%':
                return int(salario*0.31)
            elif elemento[2] == '36%':
                return int(salario*0.36)        
    return "Salario invalido o muy superior" 


def main():
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
    while True:
        salario = int(input('Ingrese un salario nominal mensual (0 para finalizar ) : '))
        if salario == 0:
            break
        print(f'El IRPF para un salario mensual de ${salario} es ${calculo_irpf(ListasAlumnos, salario)}.')



if __name__=='__main__':
    main()



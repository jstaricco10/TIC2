"""" 1 Escribir una función romano(n) que recibe como argumento un número entero entre 1 y 3999
y retorna el string correspondiente a su numeración romana.  Por ejemplo romano(9) es 'IX'."""

"""I - 1  , V - 5  X - 10 ,  L - 50, C - 100, D -500,  M-1000  """


# debemos ver por unidades, decenas, centenas y miles e ir encadenando
def switcherUnidades(argument):
    switcher = {
        0: "",
        1: "I",
        2: "II",
        3: "III",
        4: "IV",
        5: "V",
        6: "VI",
        7: "VII",
        8: "VIII",
        9: "IX",
    }
    return switcher.get(argument, "")


def switcherDecenas(argument):
    switcher = {
        1: "X",
        2: "XX",
        3: "XXX",
        4: "XL",
        5: "L",
        6: "LX",
        7: "LXX",
        8: "LXXX",
        9: "XC",
    }
    return switcher.get(argument,"")

def switcherCentenas(argument):
    switcher = {
        1: "C",
        2: "CC",
        3: "CCC",
        4: "CD",
        5: "D",
        6: "DC",
        7: "DCC",
        8: "DCCC",
        9: "CM",
    }
    return switcher.get(argument,"")


def switcherMiles(argument):
    switcher = {
        1: "M",
        2: "MM",
        3: "MMM",
    }
    return switcher.get(argument,"")


def romano(m):
    romano = ""
    n = m #n es simplemente una variable para operar en el valor de m sin perderlo

    unidades = n % 10
    int(unidades)
    n = n - unidades
    n = n / 10

    decenas = n % 10
    int(decenas)
    n = n - decenas
    n = n / 10

    centenas = n % 10
    int(centenas)
    n = n - centenas
    n = n / 10

    miles = n % 10
    int(miles)
    n = n - miles
    n = n / 10
    if 0 < m < 9:
        romano = str(switcherUnidades(unidades))
    elif 10 < m < 99:
        romano = str(switcherDecenas(decenas)) + str(switcherUnidades(unidades))
    elif 100 < m < 999:
        romano = str(switcherCentenas(centenas)) + str(switcherDecenas(decenas)) + str(switcherUnidades(unidades))
    elif 1000 < m < 3999:
        romano = str(switcherMiles(miles)) + str(switcherCentenas(centenas)) + str(switcherDecenas(decenas)) + str(switcherUnidades(unidades))

    return romano


print(romano(1999))





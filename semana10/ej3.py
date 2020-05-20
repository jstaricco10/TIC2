# ej3.py


""" Escribir un programa que pregunta por un verbo regular (con la función input()) y escribe la conjugación.
Por ej, esta sería la conjugación de los verbos amAR, temER, partIR,
para las seis personas Yo/Tú/Él,ella/Nosotros/Vosotros/Ellos.
# 1ra conjugación: AMar: AMo AMas AMa AMamos AMáis AMan
# 2da conjugación: TEMer: TEMo TEMes TEMe TEMemos TEMéis TEMen
# 3ra conjugación: PARTir: PARTo PARTes PARTe PARTimos PARTís PARTen """


# Le sacamos el ultimo r al verbo y le introducimos las terminaciones

# la otra opcion es acceder al largo, sacarle la ulitma posicion e introducir la terminacion, replace ultima posicion
# con la terminacion

def conjugar(verbo):
    tamano = len(verbo)
    if verbo[-2] == "a":
        print("Yo " + verbo[:tamano-2] + "o")
        print("Tu " + verbo[:tamano - 2] + "as")
        print("El/Ella " + verbo[:tamano - 2] + "a")
        print("Nostros " + verbo[:tamano - 2] + "amos")
        print("Ustedes " + verbo[:tamano - 2] + "ais")
        print("Ellos/Ellas " + verbo[:tamano - 2] + "an")
    elif verbo[-2] == "e":
        print("Yo " + verbo[:tamano - 2] + "o")
        print("Tu " + verbo[:tamano - 2] + "es")
        print("El/Ella " + verbo[:tamano - 2] + "e")
        print("Nostros " + verbo[:tamano - 2] + "emos")
        print("Ustedes " + verbo[:tamano - 2] + "eis")
        print("Ellos/Ellas " + verbo[:tamano - 2] + "en")
    elif verbo[-2] == "i":
        print("Yo " + verbo[:tamano - 2] + "o")
        print("Tu " + verbo[:tamano - 2] + "es")
        print("El/Ella " + verbo[:tamano - 2] + "e")
        print("Nostros " + verbo[:tamano - 2] + "imos")
        print("Ustedes " + verbo[:tamano - 2] + "is")
        print("Ellos/Ellas " + verbo[:tamano - 2] + "en")
    else:
        print("Verbo invalido")


conjugar(input('Introduzca un verbo a conjugar> '))


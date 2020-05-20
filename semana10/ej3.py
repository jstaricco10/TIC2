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
    arr = [char for char in verbo]
    tamano = len(arr)
    primera = verbo.replace(arr[tamano-2]+arr[tamano-1], "o")
    return primera

print(conjugar("amar"))


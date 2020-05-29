# !/usr/bin/env python3
letras = "ñáéíóúüÑÁÉÍÓÚÜ"

print(letras.encode('utf8'))
""" Retornar la posición n de un string de bytes versus retornar la posición de un string Unicode, 
¿sería más costoso en términos de ciclos de CPU y accesos a memoria, menos costoso o igualmente costoso?
 Justifique la respuesta. """

""" Un string de bytes Unicode seria mas costoso ya que es mas grande, mas pesado, tiene mas de un byte y 
 por lo tanto seria mas costoso ir a buscarlo."""
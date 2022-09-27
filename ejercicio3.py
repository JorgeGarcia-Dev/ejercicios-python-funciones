"""
Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python
tiene la función len() incorporada, pero escribirla por nosotros mismos resulta un muy buen
ejercicio.
"""

def largor(entrada):
    contador = 0
    for i in entrada:
        contador += 1
    return contador

print(largor("Programador"))
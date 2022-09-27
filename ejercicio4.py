"""
Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario
devuelve False.
"""

def vocales(vocal):
    if vocal == 'a' or vocal == 'e' or vocal == 'i' or vocal =='o' or vocal == 'u':
        print(True)
    else:
        print(False)

vocal = input("Ingresa una letra: ")

vocales(vocal)
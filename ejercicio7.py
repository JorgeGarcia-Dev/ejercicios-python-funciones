"""
Definir una función es_palindromo() que reconoce palíndromos
(es decir, palabras que tienen el mismo aspecto escritas invertidas),
ejemplo: es_palindromo ("radar") tendría que devolver True.
"""

def es_palindromo(palabra):
    if (palabra) == str(palabra) [::-1]:
        print(True)
    else:
        print(False)

palabra = input('Ingresa una palabra: ')

es_palindromo(palabra)
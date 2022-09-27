"""
Definir una función superposicion() que tome dos listas
y devuelva True si tienen al menos 1 miembro en común o devuelva False de lo contrario.
Escribir la función usando el bucle for anidado.
"""

def superposicion(lista_uno,lista_dos):
    for n in lista_uno:
        for n2 in lista_dos:
            if n == n2:
                return True
    return False

lista_uno = ['a', 'b', 'c', 'd', 'f']
lista_dos = ['a', 'e', 'i', 'o', 'u']

print(superposicion(lista_uno, lista_dos))
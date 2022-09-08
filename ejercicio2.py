"""
Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el
mayor de ellos. 
"""

def max(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        print("El número mayor es: ", num1)
    elif num2 >= num1 and num2 >= num3:
        print("El número mayor es: ", num2)
    else:
        print("El número mayor es: ", num3)

num1 = int(input("Ingresa un número: "))
num2 = int(input("Ingresa un segundo número: "))
num3 = int(input("Ingresa un tercer número: "))

max(num1, num2, num3)
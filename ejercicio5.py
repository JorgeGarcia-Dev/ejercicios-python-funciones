"""
Escribir una funcion sum() y una función multip() que sumen y multipliquen respectivamente
todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4])
debería devolver 24.
"""

def suma(lista):

    x = 0
    for i in range(0,len(lista)):
        x = int(lista[i])+x
    print(x)



def multip(lista):
	
	x = 1
	for i in range(0,len(lista)):
		x = int(lista[i])*x
	print(x)

suma([1,2,3,4])
multip([1,2,3,4])
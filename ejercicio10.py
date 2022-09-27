"""
Definir un histograma procedimiento() que tome una lista de números enteros e imprima un histograma en la pantalla.
Ejemplo: procedimiento([4, 9, 7]) debería imprimir lo siguiente:
****
*********
*******
"""

def procedimiento(datos):

	listado = list(datos)
	for i in listado:
		print("*" * int(i))

datos = [5, 3, 8, 2, 9, 1]
procedimiento(datos)
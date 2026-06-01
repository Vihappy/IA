def ordenamiento_intercambio(valores):
	"""
	Ordena una lista usando intercambio (burbuja).

	Parametros:
	- valores: iterable de numeros comparables.

	Retorna:
	- Nueva lista ordenada en forma ascendente.
	"""
	arr = list(valores)  # Copia los valores para ordenar.
	n = len(arr)  # Tamano del arreglo.
	for i in range(n - 1):  # Cada pasada fija el mayor al final.
		hubo_cambio = False  # Bandera para cortar si ya esta ordenado.
		for j in range(0, n - i - 1):  # Recorre la parte no ordenada.
			if arr[j] > arr[j + 1]:  # Compara elementos adyacentes.
				arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Intercambia si estan mal.
				hubo_cambio = True  # Marca que hubo un intercambio.
		if not hubo_cambio:  # Si no hubo cambios, ya esta ordenado.
			break  # Sale del ciclo principal.
	return arr  # Devuelve la lista ordenada.


if __name__ == "__main__":  # Punto de entrada para ejecutar el ejemplo.
	datos = [5, 1, 4, 2, 8, 0, 2]  # Datos de prueba.
	print("Original:", datos)  # Muestra la lista original.
	print("Ordenado:", ordenamiento_intercambio(datos))  # Muestra la lista ordenada.

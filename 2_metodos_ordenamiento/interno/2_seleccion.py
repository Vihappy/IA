def ordenamiento_seleccion(valores):
	"""
	Ordena una lista usando seleccion directa.

	Parametros:
	- valores: iterable de numeros comparables.

	Retorna:
	- Nueva lista ordenada en forma ascendente.
	"""
	arr = list(valores)  # Copia los valores para trabajar sobre ellos.
	n = len(arr)  # Guarda el tamano de la lista.
	for i in range(n):  # Recorre cada posicion a fijar.
		indice_min = i  # Supone el minimo en la posicion actual.
		for j in range(i + 1, n):  # Busca el minimo en el resto del arreglo.
			if arr[j] < arr[indice_min]:  # Compara con el minimo actual.
				indice_min = j  # Actualiza el indice del minimo.
		arr[i], arr[indice_min] = arr[indice_min], arr[i]  # Intercambia posiciones.
	return arr  # Devuelve la lista ordenada.


if __name__ == "__main__":  # Punto de entrada para ejecutar el ejemplo.
	datos = [9, 1, 6, 2, 8, 5, 3, 7, 4]  # Datos de prueba.
	print("Original:", datos)  # Muestra la lista original.
	print("Ordenado:", ordenamiento_seleccion(datos))  # Muestra la lista ordenada.

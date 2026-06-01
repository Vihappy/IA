def ordenamiento_insercion(valores):
	"""
	Ordena una lista usando insercion directa.

	Parametros:
	- valores: iterable de numeros comparables.

	Retorna:
	- Nueva lista ordenada en forma ascendente.
	"""
	arr = list(valores)  # Copia los valores para no modificar el original.
	for i in range(1, len(arr)):  # Recorre desde el segundo elemento.
		temp = arr[i]  # Guarda el valor actual a insertar.
		j = i - 1  # Apunta al elemento anterior.
		while j >= 0 and arr[j] > temp:  # Desplaza mayores a la derecha.
			arr[j + 1] = arr[j]  # Mueve el elemento una posicion.
			j -= 1  # Retrocede el indice para seguir comparando.
		arr[j + 1] = temp  # Inserta el valor en su posicion.
	return arr  # Devuelve la lista ordenada.


if __name__ == "__main__":  # Punto de entrada para ejecutar el ejemplo.
	datos = [8, 3, 5, 4, 7, 6, 2, 1]  # Datos de prueba.
	print("Original:", datos)  # Muestra la lista original.
	print("Ordenado:", ordenamiento_insercion(datos))  # Muestra la lista ordenada.

def _particionar(arr, inicio, fin):  # Particiona el arreglo alrededor del pivote.
	pivote = arr[fin]  # Selecciona el pivote como el ultimo elemento.
	i = inicio - 1  # Indice para los elementos menores al pivote.
	for j in range(inicio, fin):  # Recorre el segmento a particionar.
		if arr[j] <= pivote:  # Si el elemento va a la izquierda del pivote.
			i += 1  # Avanza el indice de menores.
			arr[i], arr[j] = arr[j], arr[i]  # Intercambia elementos.
	arr[i + 1], arr[fin] = arr[fin], arr[i + 1]  # Coloca el pivote en su lugar.
	return i + 1  # Devuelve la posicion final del pivote.


def _quicksort(arr, inicio, fin):  # Ordena recursivamente el arreglo.
	if inicio < fin:  # Verifica que el segmento tenga al menos dos elementos.
		pivote = _particionar(arr, inicio, fin)  # Particiona y obtiene el pivote.
		_quicksort(arr, inicio, pivote - 1)  # Ordena la parte izquierda.
		_quicksort(arr, pivote + 1, fin)  # Ordena la parte derecha.


def quicksort(valores):
	"""
	Ordena una lista usando QuickSort.

	Parametros:
	- valores: iterable de numeros comparables.

	Retorna:
	- Nueva lista ordenada en forma ascendente.
	"""
	arr = list(valores)  # Copia los valores para no modificar el original.
	if arr:  # Si hay elementos, aplica el algoritmo.
		_quicksort(arr, 0, len(arr) - 1)  # Ordena toda la lista.
	return arr  # Devuelve la lista ordenada.


if __name__ == "__main__":  # Punto de entrada para ejecutar el ejemplo.
	datos = [10, 7, 8, 9, 1, 5]  # Datos de prueba.
	print("Original:", datos)  # Muestra la lista original.
	print("Ordenado:", quicksort(datos))  # Muestra la lista ordenada.

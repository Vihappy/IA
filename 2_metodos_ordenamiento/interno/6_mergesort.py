def _mezclar(izq, der):  # Mezcla dos listas ordenadas.
	resultado = []  # Lista donde se acumula el resultado.
	i = 0  # Indice para la lista izquierda.
	j = 0  # Indice para la lista derecha.
	while i < len(izq) and j < len(der):  # Compara mientras haya elementos.
		if izq[i] <= der[j]:  # Toma el menor de los dos.
			resultado.append(izq[i])  # Agrega el elemento de la izquierda.
			i += 1  # Avanza en la izquierda.
		else:
			resultado.append(der[j])  # Agrega el elemento de la derecha.
			j += 1  # Avanza en la derecha.
	resultado.extend(izq[i:])  # Agrega lo que quede en la izquierda.
	resultado.extend(der[j:])  # Agrega lo que quede en la derecha.
	return resultado  # Devuelve la lista mezclada.


def mergesort(valores):
	"""
	Ordena una lista usando MergeSort.

	Parametros:
	- valores: iterable de numeros comparables.

	Retorna:
	- Nueva lista ordenada en forma ascendente.
	"""
	arr = list(valores)  # Copia los valores para no modificar el original.
	if len(arr) <= 1:  # Caso base: lista vacia o de un elemento.
		return arr  # Ya esta ordenada.
	medio = len(arr) // 2  # Divide en dos mitades.
	izq = mergesort(arr[:medio])  # Ordena la mitad izquierda.
	der = mergesort(arr[medio:])  # Ordena la mitad derecha.
	return _mezclar(izq, der)  # Mezcla y devuelve el resultado.


if __name__ == "__main__":  # Punto de entrada para ejecutar el ejemplo.
	datos = [38, 27, 43, 3, 9, 82, 10]  # Datos de prueba.
	print("Original:", datos)  # Muestra la lista original.
	print("Ordenado:", mergesort(datos))  # Muestra la lista ordenada.

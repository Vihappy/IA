def _radix_no_neg(arr):  # Ordena enteros no negativos por digitos.
	if not arr:  # Si no hay elementos, retorna vacio.
		return []  # Devuelve una lista vacia.

	maximo = max(arr)  # Encuentra el valor maximo para saber cuantos digitos usar.
	exp = 1  # Exponente que indica el digito a evaluar.
	salida = list(arr)  # Copia de trabajo para la ordenacion estable.

	while maximo // exp > 0:  # Repite por cada digito.
		conteo = [0] * 10  # Arreglo de conteo para base 10.
		for valor in salida:  # Cuenta ocurrencias del digito actual.
			indice = (valor // exp) % 10  # Obtiene el digito.
			conteo[indice] += 1  # Incrementa el conteo.
		for i in range(1, 10):  # Acumula posiciones finales.
			conteo[i] += conteo[i - 1]  # Suma acumulada.

		siguiente = [0] * len(salida)  # Salida temporal ordenada por el digito.
		for valor in reversed(salida):  # Recorre en reversa para estabilidad.
			indice = (valor // exp) % 10  # Obtiene el digito.
			conteo[indice] -= 1  # Reserva la posicion.
			siguiente[conteo[indice]] = valor  # Coloca el valor en su lugar.

		salida = siguiente  # Actualiza la salida para el siguiente digito.
		exp *= 10  # Pasa al siguiente digito.

	return salida  # Devuelve la lista ordenada.


def radixsort(valores):
	"""
	Ordena enteros usando RadixSort (base 10).

	Parametros:
	- valores: iterable de enteros.

	Retorna:
	- Nueva lista ordenada en forma ascendente.
	"""
	arr = list(valores)  # Copia los valores para no modificar el original.
	if any(not isinstance(v, int) for v in arr):  # Valida que sean enteros.
		raise ValueError("RadixSort solo acepta enteros")  # Lanza error si no.

	negativos = [-v for v in arr if v < 0]  # Convierte negativos a positivos.
	positivos = [v for v in arr if v >= 0]  # Separa los no negativos.

	ordenados_pos = _radix_no_neg(positivos)  # Ordena los positivos.
	ordenados_neg = _radix_no_neg(negativos)  # Ordena los negativos en valor abs.
	ordenados_neg = [-v for v in reversed(ordenados_neg)]  # Restaura signo y orden.

	return ordenados_neg + ordenados_pos  # Combina negativos y positivos.


if __name__ == "__main__":  # Punto de entrada para ejecutar el ejemplo.
	datos = [170, 45, 75, -90, 802, 24, 2, 66]  # Datos de prueba.
	print("Original:", datos)  # Muestra la lista original.
	print("Ordenado:", radixsort(datos))  # Muestra la lista ordenada.

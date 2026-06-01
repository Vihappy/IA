def _mezclar(izq, der):  # Mezcla dos corridas ordenadas.
	resultado = []  # Lista donde se guarda el resultado.
	i = 0  # Indice para la corrida izquierda.
	j = 0  # Indice para la corrida derecha.
	while i < len(izq) and j < len(der):  # Compara mientras haya elementos.
		if izq[i] <= der[j]:  # Toma el menor elemento.
			resultado.append(izq[i])  # Agrega desde la izquierda.
			i += 1  # Avanza en la izquierda.
		else:
			resultado.append(der[j])  # Agrega desde la derecha.
			j += 1  # Avanza en la derecha.
	resultado.extend(izq[i:])  # Agrega lo restante de la izquierda.
	resultado.extend(der[j:])  # Agrega lo restante de la derecha.
	return resultado  # Devuelve la mezcla ordenada.


def ordenamiento_polifase(valores, tam_bloque=4):
	"""
	Simula el ordenamiento polifase en memoria con corridas iniciales.

	Parametros:
	- valores: iterable de numeros comparables.
	- tam_bloque: tamano inicial de cada corrida.

	Retorna:
	- Nueva lista ordenada en forma ascendente.
	"""
	arr = list(valores)  # Copia los valores para no modificar el original.
	corridas = [sorted(arr[i:i + tam_bloque]) for i in range(0, len(arr), tam_bloque)]  # Genera corridas iniciales.

	cinta_a = corridas[::2]  # Distribuye corridas en la cinta A.
	cinta_b = corridas[1::2]  # Distribuye corridas en la cinta B.

	while len(cinta_a) + len(cinta_b) > 1:  # Repite hasta quedar una corrida.
		salida = []  # Cinta de salida para la fase actual.
		while cinta_a or cinta_b:  # Mezcla corridas mientras haya en alguna cinta.
			if cinta_a and cinta_b:  # Si hay corridas en ambas cintas.
				salida.append(_mezclar(cinta_a.pop(0), cinta_b.pop(0)))  # Mezcla una de cada.
			elif cinta_a:
				salida.append(cinta_a.pop(0))  # Pasa la corrida restante de A.
			else:
				salida.append(cinta_b.pop(0))  # Pasa la corrida restante de B.

		cinta_a = salida[::2]  # Redistribuye la salida en la cinta A.
		cinta_b = salida[1::2]  # Redistribuye la salida en la cinta B.

	if cinta_a:  # Si queda una corrida en A, es el resultado.
		return cinta_a[0]  # Devuelve la corrida final.
	if cinta_b:  # Si queda una corrida en B, es el resultado.
		return cinta_b[0]  # Devuelve la corrida final.
	return []  # Si no hay corridas, retorna vacio.


if __name__ == "__main__":  # Punto de entrada para ejecutar el ejemplo.
	datos = [20, 7, 1, 18, 4, 12, 3, 9, 15, 6, 2, 11]  # Datos de prueba.
	print("Original:", datos)  # Muestra la lista original.
	print("Ordenado:", ordenamiento_polifase(datos, tam_bloque=3))  # Muestra la lista ordenada.

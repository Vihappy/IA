import heapq  # Libreria para manejar una cola de prioridad.


def _mezcla_k(corridas):  # Mezcla k corridas usando un heap.
	heap = []  # Cola de prioridad con el menor elemento de cada corrida.
	for indice, corrida in enumerate(corridas):  # Recorre cada corrida.
		if corrida:  # Si la corrida no esta vacia.
			heapq.heappush(heap, (corrida[0], indice, 0))  # Inserta el primer elemento.

	salida = []  # Lista donde se acumula el resultado.
	while heap:  # Mientras haya elementos en el heap.
		valor, idx_corrida, idx_valor = heapq.heappop(heap)  # Extrae el menor.
		salida.append(valor)  # Agrega el menor a la salida.
		siguiente = idx_valor + 1  # Calcula el siguiente indice en la corrida.
		if siguiente < len(corridas[idx_corrida]):  # Si la corrida tiene mas elementos.
			heapq.heappush(heap, (corridas[idx_corrida][siguiente], idx_corrida, siguiente))  # Inserta el siguiente.

	return salida  # Devuelve la lista mezclada.


def mezcla_balanceada_multivias(valores, tam_bloque=4, k=3):
	"""
	Ordena usando mezcla balanceada multivias.

	Parametros:
	- valores: iterable de numeros comparables.
	- tam_bloque: tamano inicial de cada corrida.
	- k: numero de vias para mezclar en cada fase.

	Retorna:
	- Nueva lista ordenada en forma ascendente.
	"""
	arr = list(valores)  # Copia los valores para no modificar el original.
	corridas = [sorted(arr[i:i + tam_bloque]) for i in range(0, len(arr), tam_bloque)]  # Genera corridas iniciales.

	while len(corridas) > 1:  # Repite hasta una sola corrida.
		nuevas = []  # Lista de corridas mezcladas.
		for i in range(0, len(corridas), k):  # Mezcla k corridas a la vez.
			nuevas.append(_mezcla_k(corridas[i:i + k]))  # Mezcla el grupo actual.
		corridas = nuevas  # Actualiza la lista de corridas.

	return corridas[0] if corridas else []  # Devuelve la corrida final.


if __name__ == "__main__":  # Punto de entrada para ejecutar el ejemplo.
	datos = [15, 3, 12, 6, 9, 1, 8, 4, 7, 2, 5, 11, 10, 14, 13]  # Datos de prueba.
	print("Original:", datos)  # Muestra la lista original.
	print("Ordenado:", mezcla_balanceada_multivias(datos, tam_bloque=3, k=3))  # Muestra la lista ordenada.

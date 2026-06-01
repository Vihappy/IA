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


def _corridas_naturales(arr):  # Detecta corridas ya ordenadas.
	if not arr:  # Si no hay datos, retorna vacio.
		return []  # Devuelve lista vacia.

	corridas = []  # Almacena todas las corridas.
	actual = [arr[0]]  # Inicia la corrida con el primer elemento.
	for valor in arr[1:]:  # Recorre el resto de elementos.
		if valor >= actual[-1]:  # Si mantiene el orden ascendente.
			actual.append(valor)  # Agrega a la corrida actual.
		else:
			corridas.append(actual)  # Cierra la corrida actual.
			actual = [valor]  # Inicia una nueva corrida.
	corridas.append(actual)  # Agrega la ultima corrida.
	return corridas  # Devuelve la lista de corridas.


def mezcla_natural(valores):
	"""
	Ordena usando mezcla natural (natural merging).

	Parametros:
	- valores: iterable de numeros comparables.

	Retorna:
	- Nueva lista ordenada en forma ascendente.
	"""
	arr = list(valores)  # Copia los valores para no modificar el original.
	corridas = _corridas_naturales(arr)  # Genera corridas naturales.

	while len(corridas) > 1:  # Repite hasta obtener una sola corrida.
		nuevas = []  # Lista de corridas mezcladas.
		for i in range(0, len(corridas), 2):  # Mezcla de dos en dos.
			if i + 1 < len(corridas):  # Si hay pareja para mezclar.
				nuevas.append(_mezclar(corridas[i], corridas[i + 1]))  # Mezcla corridas.
			else:
				nuevas.append(corridas[i])  # Si sobra una, pasa sin cambios.
		corridas = nuevas  # Actualiza las corridas.

	return corridas[0] if corridas else []  # Devuelve la corrida final.


if __name__ == "__main__":  # Punto de entrada para ejecutar el ejemplo.
	datos = [1, 3, 5, 2, 4, 6, 0, 7]  # Datos de prueba.
	print("Original:", datos)  # Muestra la lista original.
	print("Ordenado:", mezcla_natural(datos))  # Muestra la lista ordenada.

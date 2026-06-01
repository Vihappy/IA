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


def mezcla_directa(valores, tam_bloque=4):
	"""
	Ordena usando mezcla directa (straight merging) con corridas de tam_bloque.

	Parametros:
	- valores: iterable de numeros comparables.
	- tam_bloque: tamano inicial de cada corrida.

	Retorna:
	- Nueva lista ordenada en forma ascendente.
	"""
	arr = list(valores)  # Copia los valores para no modificar el original.
	corridas = [sorted(arr[i:i + tam_bloque]) for i in range(0, len(arr), tam_bloque)]  # Crea corridas iniciales.

	while len(corridas) > 1:  # Repite hasta quedar una sola corrida.
		nuevas = []  # Lista para las corridas mezcladas.
		for i in range(0, len(corridas), 2):  # Mezcla de dos en dos.
			if i + 1 < len(corridas):  # Si hay pareja, se mezcla.
				nuevas.append(_mezclar(corridas[i], corridas[i + 1]))  # Mezcla dos corridas.
			else:
				nuevas.append(corridas[i])  # Si sobra una, pasa sin cambios.
		corridas = nuevas  # Actualiza la lista de corridas.

	return corridas[0] if corridas else []  # Devuelve la corrida final.


if __name__ == "__main__":  # Punto de entrada para ejecutar el ejemplo.
	datos = [12, 3, 7, 1, 9, 2, 8, 5, 4, 6]  # Datos de prueba.
	print("Original:", datos)  # Muestra la lista original.
	print("Ordenado:", mezcla_directa(datos, tam_bloque=3))  # Muestra la lista ordenada.

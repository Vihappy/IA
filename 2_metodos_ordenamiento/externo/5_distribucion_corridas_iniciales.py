def distribucion_corridas_iniciales(valores, tam_memoria=4):
	"""
	Genera corridas iniciales ordenadas para un ordenamiento externo.

	Parametros:
	- valores: iterable de numeros comparables.
	- tam_memoria: tamano de memoria disponible para cada corrida.

	Retorna:
	- Lista de corridas (listas) ordenadas.
	"""
	arr = list(valores)  # Copia los valores para no modificar el original.
	corridas = []  # Lista para almacenar cada corrida ordenada.
	for i in range(0, len(arr), tam_memoria):  # Recorre por bloques de memoria.
		corrida = sorted(arr[i:i + tam_memoria])  # Ordena cada bloque.
		corridas.append(corrida)  # Guarda la corrida ordenada.
	return corridas  # Devuelve la lista de corridas.


if __name__ == "__main__":  # Punto de entrada para ejecutar el ejemplo.
	datos = [9, 4, 7, 3, 2, 8, 5, 1, 6]  # Datos de prueba.
	print("Original:", datos)  # Muestra la lista original.
	print("Corridas:", distribucion_corridas_iniciales(datos, tam_memoria=3))  # Muestra corridas.

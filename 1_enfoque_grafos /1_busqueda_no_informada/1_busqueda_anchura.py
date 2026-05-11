from collections import deque


def busqueda_anchura(grafo, inicio):
	"""
	Recorre un grafo usando Búsqueda en Anchura (BFS).

	Parámetros:
	- grafo: diccionario donde cada clave es un nodo y su valor es la lista de vecinos.
	- inicio: nodo desde el cual empieza el recorrido.

	Retorna:
	- Lista con el orden en que se visitan los nodos.
	"""
	visitados = set()      # Guarda nodos ya procesados
	orden = []             # Guarda el orden final del recorrido
	cola = deque([inicio]) # Cola FIFO para explorar por niveles

	while cola:
		nodo = cola.popleft()

		# Si ya fue visitado, se salta para evitar ciclos
		if nodo in visitados:
			continue

		visitados.add(nodo)
		orden.append(nodo)

		# Se agregan vecinos no visitados al final de la cola
		for vecino in grafo.get(nodo, []):
			if vecino not in visitados:
				cola.append(vecino)

	return orden


if __name__ == "__main__":
	# Representación simple de un grafo con cartas de naipes
	grafo_ejemplo = {
		"As_Corazones": ["Rey_Corazones", "As_Picas"],
		"Rey_Corazones": ["Reina_Corazones", "Rey_Diamantes"],
		"As_Picas": ["Rey_Picas"],
		"Reina_Corazones": [],
		"Rey_Diamantes": ["Reina_Diamantes"],
		"Rey_Picas": [],
		"Reina_Diamantes": []
	}

	recorrido = busqueda_anchura(grafo_ejemplo, "As_Corazones")
	print("Recorrido BFS desde As_Corazones:", recorrido)

def busqueda_profundidad(grafo, inicio):
    """
    Recorre un grafo usando Búsqueda en Profundidad (DFS).

    Parámetros:
    - grafo: diccionario donde cada clave es un nodo y su valor es la lista de vecinos.
    - inicio: nodo desde el cual empieza el recorrido.

    Retorna:
    - Lista con el orden en que se visitan los nodos.
    """
    visitados = set()  # Evita visitar el mismo nodo más de una vez
    orden = []         # Guarda el orden final de visita

    def dfs(nodo):
        # Caso base: si ya se visitó, no se procesa de nuevo
        if nodo in visitados:
            return

        visitados.add(nodo)
        orden.append(nodo)

        # Explora cada vecino antes de regresar (profundidad)
        for vecino in grafo.get(nodo, []):
            dfs(vecino)

    dfs(inicio)
    return orden


if __name__ == "__main__":
    # Grafo de ejemplo con cartas de naipes (lista de adyacencia)
    grafo_ejemplo = {
        "As_Corazones": ["Rey_Corazones", "As_Picas"],
        "Rey_Corazones": ["Reina_Corazones", "Rey_Diamantes"],
        "As_Picas": ["Rey_Picas"],
        "Reina_Corazones": ["Jota_Corazones"],
        "Rey_Diamantes": ["Reina_Diamantes"],
        "Rey_Picas": [],
        "Jota_Corazones": [],
        "Reina_Diamantes": []
    }

    recorrido = busqueda_profundidad(grafo_ejemplo, "As_Corazones")
    print("Recorrido DFS desde As_Corazones:", recorrido)

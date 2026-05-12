import heapq


def busqueda_voraz(grafo, inicio, objetivo, heuristica):
    """
    Greedy Best-First Search.
    Selecciona siempre el nodo con menor h(n).
    """
    frontera = [(heuristica[inicio], inicio)]
    padres = {inicio: None}
    visitados = set()

    while frontera:
        _, nodo = heapq.heappop(frontera)

        if nodo in visitados:
            continue

        visitados.add(nodo)

        if nodo == objetivo:
            return reconstruir_camino(padres, objetivo)

        for vecino in grafo.get(nodo, []):
            if vecino not in visitados and vecino not in padres:
                padres[vecino] = nodo
                heapq.heappush(frontera, (heuristica[vecino], vecino))

    return None


def reconstruir_camino(padres, objetivo):
    camino = []
    nodo = objetivo
    while nodo is not None:
        camino.append(nodo)
        nodo = padres[nodo]
    return list(reversed(camino))


if __name__ == "__main__":
    grafo = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": ["G"],
        "F": ["G"],
        "G": [],
    }

    h = {"A": 6, "B": 4, "C": 3, "D": 6, "E": 2, "F": 1, "G": 0}

    print("Camino voraz A -> G:", busqueda_voraz(grafo, "A", "G", h))

def busqueda_en_grafos(grafo, inicio, objetivo):
    """
    Versión simple de Graph Search (BFS + conjunto de explorados).

    Evita ciclos y no expande dos veces el mismo nodo.
    Retorna camino desde inicio hasta objetivo o None si no existe.
    """
    frontera = [[inicio]]
    explorados = set()

    while frontera:
        camino = frontera.pop(0)  # Cola FIFO
        nodo = camino[-1]

        if nodo == objetivo:
            return camino

        if nodo in explorados:
            continue

        explorados.add(nodo)

        for vecino in grafo.get(nodo, []):
            if vecino not in explorados:
                nuevo_camino = camino + [vecino]
                frontera.append(nuevo_camino)

    return None


if __name__ == "__main__":
    grafo_ejemplo = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": ["G"],
        "F": [],
        "G": [],
    }

    print("Camino A -> G:", busqueda_en_grafos(grafo_ejemplo, "A", "G"))

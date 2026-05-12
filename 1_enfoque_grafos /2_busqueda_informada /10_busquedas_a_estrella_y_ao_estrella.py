import heapq


def a_estrella(grafo, inicio, objetivo, h):
    """Implementación simple de A*."""
    frontera = [(h[inicio], 0, inicio)]  # (f, g, nodo)
    padres = {inicio: None}
    costos_g = {inicio: 0}

    while frontera:
        _, g_actual, nodo = heapq.heappop(frontera)

        if nodo == objetivo:
            return reconstruir_camino(padres, objetivo), g_actual

        for vecino, costo in grafo.get(nodo, []):
            g_nuevo = g_actual + costo
            if vecino not in costos_g or g_nuevo < costos_g[vecino]:
                costos_g[vecino] = g_nuevo
                padres[vecino] = nodo
                f_nuevo = g_nuevo + h[vecino]
                heapq.heappush(frontera, (f_nuevo, g_nuevo, vecino))

    return None, None


def ao_estrella_coste(arbol_and_or, nodo, memo=None):
    """
    Versión didáctica de AO* (solo cálculo de costo mínimo en AND-OR).

    Estructura esperada por nodo:
    - "OR": lista de opciones, cada opción es (nombre, costo_arista)
    - "AND": lista de grupos, cada grupo es [(hijo, costo_arista), ...]
    """
    if memo is None:
        memo = {}
    if nodo in memo:
        return memo[nodo]

    info = arbol_and_or.get(nodo, {})
    if not info:
        memo[nodo] = 0
        return 0

    costo_or = float("inf")
    for hijo, c in info.get("OR", []):
        costo_or = min(costo_or, c + ao_estrella_coste(arbol_and_or, hijo, memo))

    costo_and = float("inf")
    for grupo in info.get("AND", []):
        total = 0
        for hijo, c in grupo:
            total += c + ao_estrella_coste(arbol_and_or, hijo, memo)
        costo_and = min(costo_and, total)

    mejor = min(costo_or, costo_and)
    memo[nodo] = mejor
    return mejor


def reconstruir_camino(padres, objetivo):
    camino = []
    nodo = objetivo
    while nodo is not None:
        camino.append(nodo)
        nodo = padres[nodo]
    return list(reversed(camino))


if __name__ == "__main__":
    grafo = {
        "A": [("B", 1), ("C", 4)],
        "B": [("D", 2), ("E", 5)],
        "C": [("F", 1)],
        "D": [],
        "E": [("G", 2)],
        "F": [("G", 3)],
        "G": [],
    }
    h = {"A": 6, "B": 4, "C": 3, "D": 4, "E": 1, "F": 2, "G": 0}

    camino, costo = a_estrella(grafo, "A", "G", h)
    print("A*: camino", camino, "costo", costo)

    arbol = {
        "S": {"OR": [("A", 2), ("B", 3)]},
        "A": {"AND": [[("C", 2), ("D", 2)]]},
        "B": {"OR": [("E", 2)]},
    }
    print("AO*: costo estimado en S:", ao_estrella_coste(arbol, "S"))

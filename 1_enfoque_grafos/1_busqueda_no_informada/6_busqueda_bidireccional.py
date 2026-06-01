from collections import deque


def busqueda_bidireccional(grafo, inicio, objetivo):
    """
    Búsqueda bidireccional en grafo no ponderado.

    Avanza desde inicio y objetivo al mismo tiempo hasta encontrar un punto común.
    Retorna un camino simple de inicio a objetivo o None si no existe.
    """
    if inicio == objetivo:
        return [inicio]

    # Fronteras de cada lado
    cola_inicio = deque([inicio])
    cola_objetivo = deque([objetivo])

    # Padres para reconstruir camino
    padre_inicio = {inicio: None}
    padre_objetivo = {objetivo: None}

    visitados_inicio = {inicio}
    visitados_objetivo = {objetivo}

    while cola_inicio and cola_objetivo:
        interseccion = _expandir_frente(
            grafo, cola_inicio, visitados_inicio, visitados_objetivo, padre_inicio
        )
        if interseccion is not None:
            return _reconstruir_camino(interseccion, padre_inicio, padre_objetivo)

        interseccion = _expandir_frente(
            grafo, cola_objetivo, visitados_objetivo, visitados_inicio, padre_objetivo
        )
        if interseccion is not None:
            return _reconstruir_camino(interseccion, padre_inicio, padre_objetivo)

    return None


def _expandir_frente(grafo, cola, visitados_propios, visitados_otro_lado, padres):
    if not cola:
        return None

    nodo = cola.popleft()
    for vecino in grafo.get(nodo, []):
        if vecino in visitados_propios:
            continue

        visitados_propios.add(vecino)
        padres[vecino] = nodo
        cola.append(vecino)

        if vecino in visitados_otro_lado:
            return vecino

    return None


def _reconstruir_camino(punto, padre_inicio, padre_objetivo):
    # Camino inicio -> punto
    izquierda = []
    actual = punto
    while actual is not None:
        izquierda.append(actual)
        actual = padre_inicio.get(actual)
    izquierda.reverse()

    # Camino punto -> objetivo (sin repetir punto)
    derecha = []
    actual = padre_objetivo.get(punto)
    while actual is not None:
        derecha.append(actual)
        actual = padre_objetivo.get(actual)

    return izquierda + derecha


if __name__ == "__main__":
    grafo_ejemplo = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B"],
        "E": ["B", "G"],
        "F": ["C", "G"],
        "G": ["E", "F", "H"],
        "H": ["G"],
    }

    camino = busqueda_bidireccional(grafo_ejemplo, "A", "H")
    print("Camino encontrado:", camino)

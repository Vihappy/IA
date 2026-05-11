def busqueda_profundidad_limitada(grafo, inicio, limite):
    """
    Recorre un grafo usando Búsqueda en Profundidad Limitada (DLS).

    Parámetros:
    - grafo: diccionario donde cada clave es un nodo y su valor es la lista de vecinos.
    - inicio: nodo desde el cual empieza el recorrido.
    - limite: profundidad máxima permitida (0 = solo el nodo inicial).

    Retorna:
    - Lista con el orden de nodos visitados hasta el límite indicado.
    """
    visitados = set()  # Evita ciclos y repeticiones
    orden = []         # Guarda el orden de visita

    def dls(nodo, profundidad_actual):
        # Si se supera el límite, se detiene la exploración
        if profundidad_actual > limite:
            return

        # Si ya se visitó en este recorrido, no se procesa de nuevo
        if nodo in visitados:
            return

        visitados.add(nodo)
        orden.append(nodo)

        # Si ya llegamos al límite, no seguimos bajando
        if profundidad_actual == limite:
            return

        # Explora vecinos aumentando la profundidad
        for vecino in grafo.get(nodo, []):
            dls(vecino, profundidad_actual + 1)

    dls(inicio, 0)
    return orden


if __name__ == "__main__":
    # Grafo de ejemplo con cartas de naipes
    grafo_ejemplo = {
        "As_Corazones": ["Rey_Corazones", "As_Picas"],
        "Rey_Corazones": ["Reina_Corazones", "Rey_Diamantes"],
        "As_Picas": ["Rey_Picas"],
        "Reina_Corazones": ["Jota_Corazones"],
        "Rey_Diamantes": ["Reina_Diamantes"],
        "Rey_Picas": ["Reina_Picas"],
        "Jota_Corazones": [],
        "Reina_Diamantes": [],
        "Reina_Picas": []
    }

    limite = 2
    recorrido = busqueda_profundidad_limitada(grafo_ejemplo, "As_Corazones", limite)

    print(f"Recorrido DLS desde As_Corazones con límite {limite}:", recorrido)

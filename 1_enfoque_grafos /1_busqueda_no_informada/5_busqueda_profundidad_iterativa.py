def busqueda_profundidad_iterativa(grafo, inicio, objetivo=None):
    """
    Búsqueda en Profundidad Iterativa (IDDFS).

    Realiza múltiples búsquedas en profundidad limitada con límites incrementales (0, 1, 2, ...).
    Garantiza encontrar la solución más corta como BFS (busqueda por anchura), pero con menor uso de memoria como DFS(busqueda en profundidad.

    Parámetros:
    - grafo: diccionario donde cada clave es un nodo y su valor es la lista de vecinos.
    - inicio: nodo desde el cual empieza la búsqueda.
    - objetivo: nodo destino (si es None, solo imprime el recorrido de cada iteración).

    Retorna:
    - Tupla (profundidad_encontrada, recorrido) donde profundidad_encontrada es el nivel donde se encontró el objetivo.
    """

    def busqueda_profundidad_limitada(nodo, limite, visitados):
        """Busca hasta una profundidad máxima. Retorna (encontrado, recorrido)."""
        if limite < 0:
            return False, []

        if nodo in visitados:
            return False, []

        visitados.add(nodo)
        recorrido = [nodo]
        encontrado = False

        # Si llegamos al objetivo, marcamos como encontrado
        if objetivo and nodo == objetivo:
            encontrado = True

        # Si no llegamos al límite, exploramos vecinos
        if limite > 0 and not encontrado:
            for vecino in grafo.get(nodo, []):
                if vecino not in visitados:
                    encontrado, recorrido_vecino = busqueda_profundidad_limitada(
                        vecino, limite - 1, visitados
                    )
                    recorrido.extend(recorrido_vecino)
                    if encontrado:
                        break

        return encontrado, recorrido

    # Itera aumentando el límite de profundidad hasta encontrar el objetivo
    profundidad = 0
    while True:
        visitados = set()
        encontrado, recorrido = busqueda_profundidad_limitada(inicio, profundidad, visitados)

        print(f"Profundidad {profundidad}: {recorrido}")

        # Si encontramos el objetivo, retornamos
        if encontrado:
            return profundidad, recorrido

        # Si no hay cambios en el recorrido, significa que alcanzamos el límite del grafo
        if len(recorrido) <= 1 and profundidad > 0:
            return None, recorrido

        profundidad += 1


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

    print("=== Búsqueda en Profundidad Iterativa ===\n")
    profundidad, recorrido = busqueda_profundidad_iterativa(grafo_ejemplo, "As_Corazones", "Reina_Diamantes")

    if profundidad is not None:
        print(f"\nObjetivo encontrado en profundidad: {profundidad}")
        print(f"Recorrido final: {recorrido}")
    else:
        print(f"\nObjetivo no encontrado")

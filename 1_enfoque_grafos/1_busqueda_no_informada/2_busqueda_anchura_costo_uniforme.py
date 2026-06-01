import heapq


def busqueda_costo_uniforme(grafo, inicio, objetivo=None):
    """
    Búsqueda por Costo Uniforme (UCS).
    
    Recorre un grafo ponderado priorizando los nodos con menor costo acumulado.
    Garantiza encontrar el camino de menor costo.

    Parámetros:
    - grafo: diccionario donde cada clave es un nodo y su valor es una lista de tuplas (vecino, costo).
    - inicio: nodo desde el cual empieza la búsqueda.
    - objetivo: nodo destino (opcional, si no se indica recorre todo).

    Retorna:
    - Tupla (orden, costos) donde orden es la lista de nodos visitados y costos es un diccionario con el costo mínimo a cada nodo.
    """
    visitados = set()              # Nodos ya procesados
    costos = {inicio: 0}           # Costo acumulado para cada nodo
    orden = []                     # Orden de visita
    cola_prioridad = [(0, inicio)] # Min-heap: (costo_total, nodo)

    while cola_prioridad:
        costo_actual, nodo = heapq.heappop(cola_prioridad)
        
        # Si ya fue visitado, se salta
        if nodo in visitados:
            continue
        
        visitados.add(nodo)
        orden.append(nodo)
        
        # Si llegamos al objetivo, terminamos la búsqueda
        if objetivo and nodo == objetivo:
            break
        
        # Se exploran vecinos con su costo
        for vecino, costo_arista in grafo.get(nodo, []):
            costo_nuevo = costo_actual + costo_arista
            
            # Si el camino nuevo es más barato o es la primera vez, se agrega a la cola
            if vecino not in costos or costo_nuevo < costos[vecino]:
                costos[vecino] = costo_nuevo
                heapq.heappush(cola_prioridad, (costo_nuevo, vecino))
    
    return orden, costos


if __name__ == "__main__":
    # Grafo con cartas de naipes y costos (simulan distancia o dificultad)
    grafo_ponderado = {
        "As_Corazones": [("Rey_Corazones", 2), ("As_Picas", 5)],
        "Rey_Corazones": [("Reina_Corazones", 3), ("Rey_Diamantes", 4)],
        "As_Picas": [("Rey_Picas", 1)],
        "Reina_Corazones": [("Reina_Diamantes", 2)],
        "Rey_Diamantes": [("Reina_Diamantes", 3)],
        "Rey_Picas": [("Reina_Diamantes", 6)],
        "Reina_Diamantes": []
    }

    # Búsqueda completa desde As_Corazones
    print("=== Búsqueda por Costo Uniforme Completa ===")
    orden, costos = busqueda_costo_uniforme(grafo_ponderado, "As_Corazones")
    print(f"Orden de visita: {orden}")
    print(f"Costos mínimos: {costos}")
    
    # Búsqueda hacia un objetivo específico
    print("\n=== Búsqueda hacia Reina_Diamantes ===")
    orden_objetivo, costos_objetivo = busqueda_costo_uniforme(grafo_ponderado, "As_Corazones", "Reina_Diamantes")
    print(f"Orden de visita: {orden_objetivo}")
    print(f"Costo mínimo al objetivo: {costos_objetivo['Reina_Diamantes']}")

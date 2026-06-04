import heapq

def prim_algorithm(graph, start_node):
    print(f"--- Iniciando Algoritmo de Prim desde el nodo '{start_node}' ---")
    
    # mst (Minimum Spanning Tree) almacena las aristas seleccionadas
    mst = []
    # visitados almacena los nodos que ya están en el MST
    visited = set([start_node])
    
    # Priority queue para elegir la arista de menor peso
    # Almacena tuplas: (peso, nodo_origen, nodo_destino)
    edges = [
        (weight, start_node, to_node)
        for to_node, weight in graph[start_node].items()
    ]
    heapq.heapify(edges)
    
    total_cost = 0
    paso = 1
    
    print(f"Paso 0: Nodos visitados: {visited}")
    print(f"Aristas disponibles: {sorted(edges)}\n")

    while edges:
        weight, from_node, to_node = heapq.heappop(edges)
        
        # Si el destino ya fue visitado, ignoramos para no formar ciclos
        if to_node not in visited:
            print(f"Paso {paso}: Seleccionamos arista ({from_node} - {to_node}) con peso {weight}")
            visited.add(to_node)
            mst.append((from_node, to_node, weight))
            total_cost += weight
            
            # Añadir las nuevas aristas adyacentes al nodo recién agregado
            for next_node, next_weight in graph[to_node].items():
                if next_node not in visited:
                    heapq.heappush(edges, (next_weight, to_node, next_node))
            
            print(f"   Nodos visitados actuales: {visited}")
            print(f"   Cola de aristas actual: {sorted(edges)}\n")
            paso += 1
            
        # Si se han visitado todos los nodos del grafo, terminamos
        if len(visited) == len(graph):
            break

    print("--- Resultado Final ---")
    print("Árbol de Expansión Mínima (Aristas):", mst)
    print("Costo Total Mínimo:", total_cost)
    return mst, total_cost

if __name__ == "__main__":
    # Grafo de ejemplo (diccionario de adyacencias)
    example_graph = {
        'A': {'B': 4, 'C': 4},
        'B': {'A': 4, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'E': 2, 'F': 4},
        'D': {'B': 5, 'E': 3},
        'E': {'C': 2, 'D': 3, 'F': 3},
        'F': {'C': 4, 'E': 3}
    }
    
    prim_algorithm(example_graph, 'A')

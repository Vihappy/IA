class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, item):
        if self.parent[item] == item:
            return item
        else:
            self.parent[item] = self.find(self.parent[item])
            return self.parent[item]

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        
        # Forman ciclo
        if xroot == yroot:
            return False
            
        # Union por rango
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1
        return True

def kruskal_algorithm(vertices, edges, is_minimum=True):
    modo = "Mínimo" if is_minimum else "Máximo"
    print(f"\n--- Iniciando Algoritmo de Kruskal ({modo}) ---")
    
    ds = DisjointSet(vertices)
    tree_edges = []
    total_cost = 0
    paso = 1
    
    # Ordenar aristas (Ascendente para Mínimo, Descendente para Máximo)
    sorted_edges = sorted(edges, key=lambda item: item[0], reverse=not is_minimum)
    
    print(f"Aristas ordenadas: {sorted_edges}\n")
    
    for weight, u, v in sorted_edges:
        # Intenta unir
        if ds.union(u, v):
            print(f"Paso {paso}: Agregada arista ({u} - {v}) con peso {weight}")
            tree_edges.append((u, v, weight))
            total_cost += weight
            paso += 1
        else:
            print(f"  [Ignorada] arista ({u} - {v}) con peso {weight} porque formaría un ciclo")
            
        # El MST tiene (V-1) aristas
        if len(tree_edges) == len(vertices) - 1:
            break

    print("\n--- Resultado Final ---")
    print("Árbol Resultante (Aristas):", tree_edges)
    print(f"Costo Total {modo}:", total_cost)
    return tree_edges, total_cost

if __name__ == "__main__":
    nodos = ['A', 'B', 'C', 'D', 'E', 'F']
    # Lista de aristas en forma (peso, origen, destino)
    aristas = [
        (4, 'A', 'B'),
        (4, 'A', 'C'),
        (2, 'B', 'C'),
        (5, 'B', 'D'),
        (2, 'C', 'E'),
        (4, 'C', 'F'),
        (3, 'D', 'E'),
        (3, 'E', 'F')
    ]
    
    # Ejecutar Mínimo
    kruskal_algorithm(nodos, aristas, is_minimum=True)
    
    # Ejecutar Máximo
    kruskal_algorithm(nodos, aristas, is_minimum=False)

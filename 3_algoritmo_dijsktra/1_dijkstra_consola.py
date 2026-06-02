import string
import random
import heapq

def generar_grafo_aleatorio(num_nodos=6, prob_arista=0.5):
    nodos = list(string.ascii_uppercase[:num_nodos])
    grafo = {nodo: {} for nodo in nodos}
    
    for i in range(num_nodos):
        for j in range(i + 1, num_nodos):
            if random.random() < prob_arista:
                peso = random.randint(1, 10)
                grafo[nodos[i]][nodos[j]] = peso
                grafo[nodos[j]][nodos[i]] = peso # Grafo no dirigido
                
    # Para asegurar que al menos haya algunas conexiones, garantizamos un camino lineal básico
    for i in range(num_nodos - 1):
        if nodos[i+1] not in grafo[nodos[i]]:
            peso = random.randint(1, 10)
            grafo[nodos[i]][nodos[i+1]] = peso
            grafo[nodos[i+1]][nodos[i]] = peso

    return grafo

def dijkstra_paso_a_paso(grafo, inicio, fin):
    print("=" * 60)
    print(f"=== INICIANDO ALGORITMO DE DIJKSTRA ===")
    print(f"Buscando el camino más corto desde '{inicio}' hasta '{fin}'\n")
    
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    padres = {nodo: None for nodo in grafo}
    
    cola_prioridad = [(0, inicio)]
    visitados = set()
    
    print("Estado inicial:")
    print(f"Distancias: {distancias}")
    print("-" * 60)
    
    paso = 1
    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)
        
        # Si ya lo visitamos, continuamos, porque heapq puede tener duplicados no actualizados
        if nodo_actual in visitados:
            continue
            
        print(f"Paso {paso}:")
        print(f"  -> Nodo actual (menor coste): '{nodo_actual}' con distancia acumulada: {distancia_actual}")
        
        if nodo_actual == fin:
            print(f"  -> ¡Se ha llegado al nodo destino '{fin}'! Terminamos la búsqueda.")
            break
            
        visitados.add(nodo_actual)
        
        for vecino, peso in grafo[nodo_actual].items():
            if vecino in visitados:
                continue
                
            nueva_distancia = distancia_actual + peso
            print(f"    - Evaluando vecino '{vecino}' (peso de la arista: {peso})")
            print(f"      Calculando posible nueva distancia: {distancia_actual} + {peso} = {nueva_distancia}")
            
            if nueva_distancia < distancias[vecino]:
                print(f"      ¡Se encontró un camino más corto hacia '{vecino}'! (Anterior: {distancias[vecino]} -> Nueva: {nueva_distancia})")
                distancias[vecino] = nueva_distancia
                padres[vecino] = nodo_actual
                heapq.heappush(cola_prioridad, (nueva_distancia, vecino))
            else:
                print(f"      El camino actual es mejor o igual (Registrado: {distancias[vecino]}). Se descarta.")
                
        print(f"  -> Actualización de distancias general: {distancias}")
        print("-" * 60)
        paso += 1
        
    camino = []
    nodo = fin
    while nodo is not None:
        camino.insert(0, nodo)
        nodo = padres[nodo]
        
    if distancias[fin] == float('inf'):
        print(f"\nNo hay un camino posible entre '{inicio}' y '{fin}'.")
    else:
        print("\n" + "=" * 60)
        print("=== RESULTADO FINAL ===")
        print(f"Camino más corto encontrado: {' -> '.join(camino)}")
        print(f"Costo total: {distancias[fin]}")
        print("=" * 60)

if __name__ == '__main__':
    grafo = generar_grafo_aleatorio(6, 0.4)
    print("GRAFO GENERADO:")
    for nodo, vecinos in grafo.items():
        print(f"  {nodo}: {vecinos}")
    print()
    
    nodos = list(grafo.keys())
    inicio = nodos[0]
    fin = nodos[-1]
    
    dijkstra_paso_a_paso(grafo, inicio, fin)

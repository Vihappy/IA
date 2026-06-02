import tkinter as tk
from tkinter import ttk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import heapq

class DijkstraGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Algoritmo de Dijkstra - Paso a Paso")
        
        # Grafo fijo similar a los ejemplos 4 y 5
        self.graph_dict = {
            'A': {'B': 4, 'C': 2},
            'B': {'A': 4, 'C': 1, 'D': 5},
            'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
            'D': {'B': 5, 'C': 8, 'E': 2, 'F': 6},
            'E': {'C': 10, 'D': 2, 'F': 2},
            'F': {'D': 6, 'E': 2}
        }
        
        self.start_node = 'A'
        self.target_node = 'F'
        
        self.G = nx.Graph()
        for u in self.graph_dict:
            for v, w in self.graph_dict[u].items():
                self.G.add_edge(u, v, weight=w)
                
        self.pos = nx.spring_layout(self.G, seed=42)
        
        self.reset_state()
        self.setup_ui()
        self.draw_graph()

    def reset_state(self):
        # Estructuras de Dijkstra
        self.distancias = {n: float('inf') for n in self.G.nodes()}
        self.distancias[self.start_node] = 0
        self.padres = {n: None for n in self.G.nodes()}
        
        self.visitados = set()
        self.cola = [(0, self.start_node)]
        
        self.camino_final = []
        self.is_finished = False
        self.current_node = None
        
        if hasattr(self, 'lbl_info'):
            self.lbl_info.config(text=f"Iniciando en {self.start_node}. Destino: {self.target_node}")
            self.btn_next.config(state=tk.NORMAL)
            self.draw_graph()

    def setup_ui(self):
        self.control_frame = ttk.Frame(self.master, padding="10")
        self.control_frame.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.btn_next = ttk.Button(self.control_frame, text="Siguiente Paso", command=self.next_step)
        self.btn_next.pack(side=tk.LEFT, padx=10)
        
        self.btn_reset = ttk.Button(self.control_frame, text="Reiniciar", command=self.reset_state)
        self.btn_reset.pack(side=tk.LEFT, padx=5)
        
        self.lbl_info = ttk.Label(self.control_frame, text=f"Iniciando en {self.start_node}. Destino: {self.target_node}", font=("Arial", 10))
        self.lbl_info.pack(side=tk.LEFT, padx=20)
        
        self.fig, self.ax = plt.subplots(figsize=(6, 5))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def draw_graph(self):
        self.ax.clear()
        
        # Colores de nodos
        node_colors = []
        for node in self.G.nodes():
            if node == self.current_node:
                node_colors.append('yellow')
            elif node in self.camino_final:
                node_colors.append('pink') # parte del camino final
            elif node in self.visitados:
                node_colors.append('lightgreen')
            else:
                node_colors.append('skyblue')
                
        nx.draw_networkx_nodes(self.G, self.pos, ax=self.ax, node_color=node_colors, node_size=500)
        
        # Etiquetas (mostrar también la distancia actual si no es inf)
        labels = {}
        for n in self.G.nodes():
            d = self.distancias[n]
            d_str = "∞" if d == float('inf') else str(d)
            labels[n] = f"{n}\n({d_str})"
            
        nx.draw_networkx_labels(self.G, self.pos, labels=labels, ax=self.ax, font_size=9)
        
        # Aristas
        nx.draw_networkx_edges(self.G, self.pos, ax=self.ax, edge_color='lightgray', width=1)
        
        edge_labels = nx.get_edge_attributes(self.G, 'weight')
        nx.draw_networkx_edge_labels(self.G, self.pos, edge_labels=edge_labels, ax=self.ax, font_size=9)
        
        # Resaltar el camino final
        if self.camino_final:
            edges_path = [(self.camino_final[i], self.camino_final[i+1]) for i in range(len(self.camino_final)-1)]
            nx.draw_networkx_edges(self.G, self.pos, edgelist=edges_path, edge_color='red', width=3, ax=self.ax)
            
        self.ax.set_title("Algoritmo de Dijkstra", fontsize=14)
        self.canvas.draw()

    def next_step(self):
        if self.is_finished:
            return
            
        while self.cola:
            dist_actual, actual = heapq.heappop(self.cola)
            
            if actual in self.visitados:
                continue
                
            self.visitados.add(actual)
            self.current_node = actual
            
            if actual == self.target_node:
                # Reconstruir camino
                camino = []
                nodo = self.target_node
                while nodo is not None:
                    camino.insert(0, nodo)
                    nodo = self.padres[nodo]
                self.camino_final = camino
                
                self.is_finished = True
                dist_total = self.distancias[self.target_node]
                self.lbl_info.config(text=f"¡Llegada a {self.target_node}! Distancia mínima: {dist_total}")
                self.btn_next.config(state=tk.DISABLED)
                self.draw_graph()
                return

            # Relajar aristas
            for vecino, peso in self.graph_dict[actual].items():
                if vecino in self.visitados:
                    continue
                nueva_dist = dist_actual + peso
                if nueva_dist < self.distancias[vecino]:
                    self.distancias[vecino] = nueva_dist
                    self.padres[vecino] = actual
                    heapq.heappush(self.cola, (nueva_dist, vecino))

            self.lbl_info.config(text=f"Visitando {actual}. Distancia actual: {dist_actual}")
            self.draw_graph()
            return
            
        self.is_finished = True
        self.current_node = None
        self.lbl_info.config(text=f"No hay ruta posible a {self.target_node}.")
        self.btn_next.config(state=tk.DISABLED)
        self.draw_graph()

if __name__ == "__main__":
    root = tk.Tk()
    app = DijkstraGUI(root)
    root.mainloop()

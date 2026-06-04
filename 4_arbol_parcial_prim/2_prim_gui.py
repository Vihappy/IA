import tkinter as tk
from tkinter import ttk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import heapq

class PrimGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Algoritmo de Prim - Paso a Paso")
        
        # Configuración de grafo genérico
        self.graph_dict = {
            'A': {'B': 4, 'C': 4},
            'B': {'A': 4, 'C': 2, 'D': 5},
            'C': {'A': 4, 'B': 2, 'E': 2, 'F': 4},
            'D': {'B': 5, 'E': 3},
            'E': {'C': 2, 'D': 3, 'F': 3},
            'F': {'C': 4, 'E': 3}
        }
        
        self.G = nx.Graph()
        for u in self.graph_dict:
            for v, w in self.graph_dict[u].items():
                self.G.add_edge(u, v, weight=w)
                
        # Layout fijo para que no salte al dibujar
        self.pos = nx.spring_layout(self.G, seed=42)
        
        # Variables de estado del algoritmo
        self.start_node = 'A'
        self.mst_edges = []
        self.visited = set([self.start_node])
        self.edges_queue = []
        for v, w in self.graph_dict[self.start_node].items():
            heapq.heappush(self.edges_queue, (w, self.start_node, v))
            
        self.is_finished = False
        
        # Interfaz de Tkinter
        self.setup_ui()
        self.draw_graph()

    def setup_ui(self):
        # Frame de controles
        self.control_frame = ttk.Frame(self.master, padding="10")
        self.control_frame.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.btn_next = ttk.Button(self.control_frame, text="Siguiente Paso", command=self.next_step)
        self.btn_next.pack(side=tk.LEFT, padx=5)
        
        self.lbl_info = ttk.Label(self.control_frame, text=f"Inicio en nodo '{self.start_node}'. Nodos visitados: {self.visited}", font=("Arial", 10))
        self.lbl_info.pack(side=tk.LEFT, padx=10)
        
        # Figura de Matplotlib
        self.fig, self.ax = plt.subplots(figsize=(6, 5))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def draw_graph(self):
        self.ax.clear()
        
        # Dibujar todos los nodos (azul normal, verde si están visitados)
        node_colors = ['green' if node in self.visited else 'skyblue' for node in self.G.nodes()]
        nx.draw_networkx_nodes(self.G, self.pos, ax=self.ax, node_color=node_colors, node_size=500)
        nx.draw_networkx_labels(self.G, self.pos, ax=self.ax, font_color='black')
        
        # Dibujar todas las aristas con color gris apagado
        nx.draw_networkx_edges(self.G, self.pos, ax=self.ax, edge_color='lightgray', width=1.5)
        
        # Etiquetas de peso de todas las aristas
        edge_labels = nx.get_edge_attributes(self.G, 'weight')
        nx.draw_networkx_edge_labels(self.G, self.pos, edge_labels=edge_labels, ax=self.ax, font_size=9)
        
        # Dibujar las aristas del MST con color rojo y mayor grosor
        if self.mst_edges:
            mst_tree_edges = [(u, v) for u, v, w in self.mst_edges]
            nx.draw_networkx_edges(self.G, self.pos, edgelist=mst_tree_edges, edge_color='red', width=3, ax=self.ax)
            
        self.ax.set_title("Arbol Parcial Mínimo (Prim)", fontsize=14)
        self.canvas.draw()

    def next_step(self):
        if self.is_finished:
            return
            
        while self.edges_queue:
            weight, u, v = heapq.heappop(self.edges_queue)
            
            if v not in self.visited:
                self.visited.add(v)
                self.mst_edges.append((u, v, weight))
                
                # Agregar nuevas aristas a la cola
                for next_node, next_weight in self.graph_dict[v].items():
                    if next_node not in self.visited:
                        heapq.heappush(self.edges_queue, (next_weight, v, next_node))
                
                self.lbl_info.config(text=f"Agregado ({u} - {v}) con peso {weight}. Nodos: {len(self.visited)}/{len(self.graph_dict)}")
                self.draw_graph()
                
                # Revisar condición de término
                if len(self.visited) == len(self.graph_dict):
                    self.is_finished = True
                    costo_total = sum(w for _, _, w in self.mst_edges)
                    self.lbl_info.config(text=f"¡Finalizado! Costo Total Mínimo: {costo_total}")
                    self.btn_next.config(state=tk.DISABLED)
                return
                
        # Caso especial si el grafo es disconexo o se agotó la cola antes
        self.is_finished = True
        self.lbl_info.config(text="Proceso finalizado (no hay más aristas alcanzables).")
        self.btn_next.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = PrimGUI(root)
    root.mainloop()

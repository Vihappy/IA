import tkinter as tk
from tkinter import ttk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Implementación de Union-Find para Kruskal
class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}

    def find(self, item):
        if self.parent[item] == item:
            return item
        self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot == yroot:
            return False
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1
        return True

class KruskalGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Algoritmo de Kruskal - Árbol Mínimo y Máximo")
        
        # Grafo de ejemplo
        self.vertices = ['A', 'B', 'C', 'D', 'E', 'F']
        self.edges_list = [
            (4, 'A', 'B'), (4, 'A', 'C'), (2, 'B', 'C'), 
            (5, 'B', 'D'), (2, 'C', 'E'), (4, 'C', 'F'), 
            (3, 'D', 'E'), (3, 'E', 'F')
        ]
        
        self.G = nx.Graph()
        self.G.add_nodes_from(self.vertices)
        for w, u, v in self.edges_list:
            self.G.add_edge(u, v, weight=w)
            
        self.pos = nx.spring_layout(self.G, seed=42)
        
        # Variables de estado
        self.reset_state()
        
        # UI
        self.setup_ui()
        self.draw_graph()

    def reset_state(self, *args):
        self.ds = DisjointSet(self.vertices)
        self.tree_edges = []
        is_min = self.mode_var.get() == "Mínimo" if hasattr(self, 'mode_var') else True
        self.sorted_edges = sorted(self.edges_list, key=lambda item: item[0], reverse=not is_min)
        self.edge_index = 0
        self.is_finished = False
        
        if hasattr(self, 'lbl_info'):
            self.lbl_info.config(text="Estado reiniciado. Selecciona 'Siguiente Paso'.")
            self.btn_next.config(state=tk.NORMAL)
        if hasattr(self, 'ax'):
            self.draw_graph()

    def setup_ui(self):
        self.control_frame = ttk.Frame(self.master, padding="10")
        self.control_frame.pack(side=tk.BOTTOM, fill=tk.X)
        
        self.mode_var = tk.StringVar(value="Mínimo")
        
        ttk.Label(self.control_frame, text="Tipo de Árbol:").pack(side=tk.LEFT, padx=5)
        self.rb_min = ttk.Radiobutton(self.control_frame, text="Mínimo", variable=self.mode_var, value="Mínimo", command=self.reset_state)
        self.rb_min.pack(side=tk.LEFT)
        self.rb_max = ttk.Radiobutton(self.control_frame, text="Máximo", variable=self.mode_var, value="Máximo", command=self.reset_state)
        self.rb_max.pack(side=tk.LEFT, padx=5)
        
        self.btn_next = ttk.Button(self.control_frame, text="Siguiente Paso", command=self.next_step)
        self.btn_next.pack(side=tk.LEFT, padx=20)
        
        self.btn_reset = ttk.Button(self.control_frame, text="Reiniciar", command=self.reset_state)
        self.btn_reset.pack(side=tk.LEFT, padx=5)
        
        self.lbl_info = ttk.Label(self.control_frame, text="Iniciando...", font=("Arial", 10))
        self.lbl_info.pack(side=tk.LEFT, padx=20)
        
        # Plot
        self.fig, self.ax = plt.subplots(figsize=(6, 5))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def draw_graph(self):
        self.ax.clear()
        
        nx.draw_networkx_nodes(self.G, self.pos, ax=self.ax, node_color='skyblue', node_size=500)
        nx.draw_networkx_labels(self.G, self.pos, ax=self.ax)
        
        # Aristas grises originales
        nx.draw_networkx_edges(self.G, self.pos, ax=self.ax, edge_color='lightgray', width=1)
        labels = nx.get_edge_attributes(self.G, 'weight')
        nx.draw_networkx_edge_labels(self.G, self.pos, edge_labels=labels, ax=self.ax, font_size=9)
        
        # Aristas seleccionadas en el MST
        if self.tree_edges:
            mst_plot = [(u, v) for u, v, w in self.tree_edges]
            color = 'blue' if self.mode_var.get() == "Mínimo" else 'red'
            nx.draw_networkx_edges(self.G, self.pos, edgelist=mst_plot, edge_color=color, width=3, ax=self.ax)
            
        self.ax.set_title(f"Árbol de Expansión {self.mode_var.get()} (Kruskal)", fontsize=14)
        self.canvas.draw()

    def next_step(self):
        if self.is_finished:
            return
            
        while self.edge_index < len(self.sorted_edges):
            weight, u, v = self.sorted_edges[self.edge_index]
            self.edge_index += 1
            
            if self.ds.union(u, v):
                self.tree_edges.append((u, v, weight))
                self.lbl_info.config(text=f"Agregada arista ({u} - {v}) [Peso: {weight}]")
                self.draw_graph()
                
                # Terminar si tenemos V-1 aristas
                if len(self.tree_edges) == len(self.vertices) - 1:
                    self.is_finished = True
                    total_cost = sum(w for _, _, w in self.tree_edges)
                    self.lbl_info.config(text=f"¡Finalizado! Costo {self.mode_var.get()}: {total_cost}")
                    self.btn_next.config(state=tk.DISABLED)
                return
            else:
                self.lbl_info.config(text=f"Ignorada arista ({u} - {v}) [Peso: {weight}] (Forma ciclo)")
                self.draw_graph()
                return

        self.is_finished = True
        self.lbl_info.config(text="Proceso finalizado.")
        self.btn_next.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = KruskalGUI(root)
    root.mainloop()

class Nodo:  # Nodo de un arbol binario de busqueda.
	def __init__(self, valor):  # Inicializa el nodo con un valor.
		self.valor = valor  # Guarda el valor del nodo.
		self.izq = None  # Referencia al hijo izquierdo.
		self.der = None  # Referencia al hijo derecho.

	def insertar(self, valor):  # Inserta un valor en el arbol.
		if valor <= self.valor:  # Decide si va al subarbol izquierdo.
			if self.izq is None:  # Si no hay hijo, lo crea.
				self.izq = Nodo(valor)  # Crea el nodo izquierdo.
			else:
				self.izq.insertar(valor)  # Inserta recursivamente a la izquierda.
		else:
			if self.der is None:  # Si no hay hijo derecho, lo crea.
				self.der = Nodo(valor)  # Crea el nodo derecho.
			else:
				self.der.insertar(valor)  # Inserta recursivamente a la derecha.

	def inorder(self, salida):  # Recorre el arbol en orden.
		if self.izq is not None:  # Visita el subarbol izquierdo.
			self.izq.inorder(salida)  # Recorre izquierda.
		salida.append(self.valor)  # Agrega el valor actual.
		if self.der is not None:  # Visita el subarbol derecho.
			self.der.inorder(salida)  # Recorre derecha.


def ordenamiento_arbol(valores):
	"""
	Ordena una lista usando ordenamiento de arbol (tree sort).

	Parametros:
	- valores: iterable de numeros comparables.

	Retorna:
	- Nueva lista ordenada en forma ascendente.
	"""
	arr = list(valores)  # Copia los valores para no modificar el original.
	if not arr:  # Si la lista esta vacia, retorna vacio.
		return []  # Devuelve una lista vacia.

	raiz = Nodo(arr[0])  # Crea la raiz con el primer valor.
	for valor in arr[1:]:  # Inserta el resto de valores.
		raiz.insertar(valor)  # Inserta en el arbol.

	salida = []  # Lista donde se acumula el recorrido.
	raiz.inorder(salida)  # Recorre en orden para obtener la lista ordenada.
	return salida  # Devuelve la lista ordenada.


if __name__ == "__main__":  # Punto de entrada para ejecutar el ejemplo.
	datos = [7, 3, 9, 1, 5, 8, 2]  # Datos de prueba.
	print("Original:", datos)  # Muestra la lista original.
	print("Ordenado:", ordenamiento_arbol(datos))  # Muestra la lista ordenada.

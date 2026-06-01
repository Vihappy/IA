def distancia_manhattan(a, b):
    """Heurística para grillas: |x1-x2| + |y1-y2|."""
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def distancia_euclidiana(a, b):
    """Heurística alternativa: distancia en línea recta."""
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    return (dx * dx + dy * dy) ** 0.5


if __name__ == "__main__":
    inicio = (1, 2)
    meta = (4, 6)

    print("Manhattan:", distancia_manhattan(inicio, meta))
    print("Euclidiana:", round(distancia_euclidiana(inicio, meta), 2))

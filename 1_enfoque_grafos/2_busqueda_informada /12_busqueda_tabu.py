def busqueda_tabu(estado_inicial, vecinos_fn, costo_fn, tam_tabu=5, max_iter=50):
    """
    Búsqueda tabú para minimización.
    Mantiene memoria corta de estados prohibidos.
    """
    actual = estado_inicial
    mejor = estado_inicial
    tabu = []

    for _ in range(max_iter):
        candidatos = [v for v in vecinos_fn(actual) if v not in tabu]
        if not candidatos:
            break

        actual = min(candidatos, key=costo_fn)

        if costo_fn(actual) < costo_fn(mejor):
            mejor = actual

        tabu.append(actual)
        if len(tabu) > tam_tabu:
            tabu.pop(0)

    return mejor, costo_fn(mejor)


if __name__ == "__main__":
    # Minimizar (x-3)^2
    def vecinos(x):
        return [x - 2, x - 1, x + 1, x + 2]

    def costo(x):
        return (x - 3) ** 2

    mejor, valor = busqueda_tabu(10, vecinos, costo)
    print("Mejor estado:", mejor)
    print("Mejor costo:", valor)

def ascension_colinas(estado_inicial, vecinos_fn, valor_fn, max_iter=100):
    """
    Hill Climbing simple: siempre toma el mejor vecino.
    """
    actual = estado_inicial

    for _ in range(max_iter):
        vecinos = vecinos_fn(actual)
        mejor_vecino = max(vecinos, key=valor_fn)

        if valor_fn(mejor_vecino) <= valor_fn(actual):
            break

        actual = mejor_vecino

    return actual, valor_fn(actual)


if __name__ == "__main__":
    # Queremos acercarnos a x = 7 maximizando -(x-7)^2
    def vecinos(x):
        return [x - 1, x + 1]

    def valor(x):
        return -((x - 7) ** 2)

    estado, puntuacion = ascension_colinas(0, vecinos, valor)
    print("Estado final:", estado)
    print("Valor final:", puntuacion)

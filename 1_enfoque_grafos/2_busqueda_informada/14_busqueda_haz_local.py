def busqueda_haz_local(estados_iniciales, vecinos_fn, valor_fn, ancho_haz=2, max_iter=30):
    """
    Local Beam Search: mantiene k mejores estados por iteración.
    """
    haz = list(estados_iniciales)

    for _ in range(max_iter):
        todos_vecinos = []
        for estado in haz:
            todos_vecinos.extend(vecinos_fn(estado))

        if not todos_vecinos:
            break

        todos_vecinos.sort(key=valor_fn, reverse=True)
        nuevo_haz = todos_vecinos[:ancho_haz]

        if nuevo_haz == haz:
            break

        haz = nuevo_haz

    mejor = max(haz, key=valor_fn)
    return mejor, valor_fn(mejor)


if __name__ == "__main__":
    # Maximizar -(x-8)^2
    def vecinos(x):
        return [x - 1, x + 1]

    def valor(x):
        return -((x - 8) ** 2)

    mejor, puntuacion = busqueda_haz_local([0, 20], vecinos, valor, ancho_haz=2)
    print("Mejor estado:", mejor)
    print("Mejor valor:", puntuacion)

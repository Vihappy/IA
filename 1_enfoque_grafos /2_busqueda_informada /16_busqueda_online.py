def busqueda_online_lineal(posicion_inicial, objetivo, obstaculos):
    """
    Ejemplo mínimo de búsqueda online en una línea de estados.

    El agente decide paso a paso con información local:
    - intenta moverse hacia el objetivo
    - si hay obstáculo, prueba el otro sentido
    """
    posicion = posicion_inicial
    recorrido = [posicion]

    for _ in range(50):
        if posicion == objetivo:
            break

        direccion = 1 if objetivo > posicion else -1
        siguiente = posicion + direccion

        if siguiente in obstaculos:
            siguiente = posicion - direccion

        posicion = siguiente
        recorrido.append(posicion)

    return recorrido


if __name__ == "__main__":
    obstaculos = {2, 3}
    ruta = busqueda_online_lineal(0, 5, obstaculos)
    print("Recorrido online:", ruta)

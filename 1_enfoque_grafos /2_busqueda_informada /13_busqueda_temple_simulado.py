import math
import random


def temple_simulado(estado_inicial, vecinos_fn, costo_fn, t_inicial=10.0, enfriamiento=0.95, min_t=0.01):
    """
    Simulated Annealing para minimización.
    """
    actual = estado_inicial
    mejor = estado_inicial
    t = t_inicial

    while t > min_t:
        vecino = random.choice(vecinos_fn(actual))
        delta = costo_fn(vecino) - costo_fn(actual)

        if delta < 0:
            actual = vecino
        else:
            prob = math.exp(-delta / t)
            if random.random() < prob:
                actual = vecino

        if costo_fn(actual) < costo_fn(mejor):
            mejor = actual

        t *= enfriamiento

    return mejor, costo_fn(mejor)


if __name__ == "__main__":
    random.seed(7)

    # Minimizar (x-5)^2
    def vecinos(x):
        return [x - 1, x + 1]

    def costo(x):
        return (x - 5) ** 2

    mejor, valor = temple_simulado(20, vecinos, costo)
    print("Mejor estado:", mejor)
    print("Mejor costo:", valor)

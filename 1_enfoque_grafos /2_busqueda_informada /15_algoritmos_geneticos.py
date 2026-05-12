import random


def fitness(x):
    # Objetivo: acercarse a 31
    return -(x - 31) ** 2


def seleccion_torneo(poblacion, k=3):
    candidatos = random.sample(poblacion, k)
    return max(candidatos, key=fitness)


def cruce(p1, p2):
    # Cruce de 6 bits
    punto = random.randint(1, 5)
    b1 = f"{p1:06b}"
    b2 = f"{p2:06b}"
    hijo = int(b1[:punto] + b2[punto:], 2)
    return hijo


def mutacion(individuo, prob=0.1):
    bits = list(f"{individuo:06b}")
    for i in range(len(bits)):
        if random.random() < prob:
            bits[i] = "1" if bits[i] == "0" else "0"
    return int("".join(bits), 2)


def algoritmo_genetico(tam=10, generaciones=30):
    poblacion = [random.randint(0, 63) for _ in range(tam)]

    for _ in range(generaciones):
        nueva = []
        for _ in range(tam):
            p1 = seleccion_torneo(poblacion)
            p2 = seleccion_torneo(poblacion)
            hijo = cruce(p1, p2)
            hijo = mutacion(hijo)
            nueva.append(hijo)
        poblacion = nueva

    mejor = max(poblacion, key=fitness)
    return mejor, fitness(mejor)


if __name__ == "__main__":
    random.seed(5)
    mejor, ajuste = algoritmo_genetico()
    print("Mejor individuo:", mejor)
    print("Fitness:", ajuste)

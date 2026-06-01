import random


def recompensa_politica(theta):
    """
    Entorno ficticio: máxima recompensa cerca de theta=2.5.
    """
    ruido = random.uniform(-0.1, 0.1)
    return -((theta - 2.5) ** 2) + 5 + ruido


def busqueda_politica(theta_inicial=0.0, pasos=100, paso=0.2):
    """Policy Search por ascenso estocástico en parámetros."""
    theta = theta_inicial
    mejor_r = recompensa_politica(theta)

    for _ in range(pasos):
        candidato = theta + random.uniform(-paso, paso)
        r = recompensa_politica(candidato)

        if r > mejor_r:
            theta = candidato
            mejor_r = r

    return theta, mejor_r


if __name__ == "__main__":
    random.seed(12)
    theta, r = busqueda_politica()
    print("Parámetro de política:", round(theta, 3))
    print("Recompensa estimada:", round(r, 3))

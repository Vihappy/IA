import random


def epsilon_greedy_bandido(recompensas_reales, pasos=200, epsilon=0.1):
    brazos = list(recompensas_reales.keys())
    estimadas = {b: 0.0 for b in brazos}
    conteos = {b: 0 for b in brazos}
    total = 0

    for _ in range(pasos):
        if random.random() < epsilon:
            b = random.choice(brazos)  # exploración
        else:
            b = max(brazos, key=lambda x: estimadas[x])  # explotación

        # Entorno determinista simple (podría ser estocástico)
        r = recompensas_reales[b]
        total += r

        conteos[b] += 1
        estimadas[b] += (r - estimadas[b]) / conteos[b]

    return estimadas, conteos, total


if __name__ == "__main__":
    random.seed(2)

    reales = {"brazo_1": 1.0, "brazo_2": 1.4, "brazo_3": 0.8}
    estimadas, conteos, total = epsilon_greedy_bandido(reales, epsilon=0.2)

    print("Estimaciones:", estimadas)
    print("Conteos:", conteos)
    print("Recompensa total:", total)

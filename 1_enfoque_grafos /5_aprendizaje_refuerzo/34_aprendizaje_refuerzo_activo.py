import random


def entorno(estado, accion):
    """Entorno mínimo de 2 estados y 2 acciones."""
    if estado == "S1" and accion == "A":
        return "S2", 1
    if estado == "S1" and accion == "B":
        return "S1", 0
    if estado == "S2" and accion == "A":
        return "S2", 2
    return "S1", -1


def elegir_accion(q, estado, acciones, epsilon):
    if random.random() < epsilon:
        return random.choice(acciones)
    return max(acciones, key=lambda a: q[(estado, a)])


def aprendizaje_activo(episodios=100, alpha=0.1, gamma=0.9, epsilon=0.2):
    acciones = ["A", "B"]
    q = {(s, a): 0.0 for s in ["S1", "S2"] for a in acciones}

    for _ in range(episodios):
        estado = "S1"
        for _ in range(10):
            accion = elegir_accion(q, estado, acciones, epsilon)
            sig, recompensa = entorno(estado, accion)
            mejor_sig = max(q[(sig, a)] for a in acciones)
            q[(estado, accion)] += alpha * (recompensa + gamma * mejor_sig - q[(estado, accion)])
            estado = sig

    return q


if __name__ == "__main__":
    random.seed(10)
    q = aprendizaje_activo()
    print("Q aprendida:", q)

import random


def q_learning(tabla_q, transicion, estados, acciones, episodios=200, alpha=0.1, gamma=0.9, epsilon=0.1):
    for _ in range(episodios):
        s = random.choice(estados)
        for _ in range(15):
            if random.random() < epsilon:
                a = random.choice(acciones)
            else:
                a = max(acciones, key=lambda x: tabla_q[(s, x)])

            s2, r = transicion(s, a)
            mejor_s2 = max(tabla_q[(s2, a2)] for a2 in acciones)
            tabla_q[(s, a)] += alpha * (r + gamma * mejor_s2 - tabla_q[(s, a)])
            s = s2

    return tabla_q


if __name__ == "__main__":
    random.seed(4)

    estados = ["A", "B"]
    acciones = ["izq", "der"]
    q = {(s, a): 0.0 for s in estados for a in acciones}

    def transicion(s, a):
        if s == "A" and a == "der":
            return "B", 5
        if s == "B" and a == "izq":
            return "A", 1
        return s, 0

    q = q_learning(q, transicion, estados, acciones)
    print("Tabla Q final:")
    for clave in sorted(q):
        print(clave, round(q[clave], 3))

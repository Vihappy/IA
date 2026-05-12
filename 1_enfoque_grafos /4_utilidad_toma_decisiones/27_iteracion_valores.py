def iteracion_valores(estados, acciones, transiciones, recompensas, gamma=0.9, theta=1e-6):
    """Value Iteration para un MDP pequeño."""
    v = {s: 0.0 for s in estados}

    while True:
        delta = 0
        nuevo_v = dict(v)

        for s in estados:
            valores_accion = []
            for a in acciones[s]:
                valor = 0
                for p, s2 in transiciones[(s, a)]:
                    valor += p * (recompensas[(s, a, s2)] + gamma * v[s2])
                valores_accion.append(valor)

            nuevo_v[s] = max(valores_accion)
            delta = max(delta, abs(nuevo_v[s] - v[s]))

        v = nuevo_v
        if delta < theta:
            break

    return v


if __name__ == "__main__":
    estados = ["S1", "S2"]
    acciones = {"S1": ["a", "b"], "S2": ["a"]}

    transiciones = {
        ("S1", "a"): [(1.0, "S1")],
        ("S1", "b"): [(1.0, "S2")],
        ("S2", "a"): [(1.0, "S2")],
    }

    recompensas = {
        ("S1", "a", "S1"): 2,
        ("S1", "b", "S2"): 5,
        ("S2", "a", "S2"): 1,
    }

    print("Valores:", iteracion_valores(estados, acciones, transiciones, recompensas))

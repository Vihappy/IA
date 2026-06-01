def evaluar_politica(estados, politica, transiciones, recompensas, gamma=0.9, theta=1e-6):
    v = {s: 0.0 for s in estados}

    while True:
        delta = 0
        for s in estados:
            a = politica[s]
            nuevo = sum(
                p * (recompensas[(s, a, s2)] + gamma * v[s2])
                for p, s2 in transiciones[(s, a)]
            )
            delta = max(delta, abs(nuevo - v[s]))
            v[s] = nuevo
        if delta < theta:
            break

    return v


def mejorar_politica(estados, acciones, transiciones, recompensas, v, gamma=0.9):
    politica = {}
    for s in estados:
        mejor_accion = None
        mejor_valor = float("-inf")
        for a in acciones[s]:
            valor = sum(
                p * (recompensas[(s, a, s2)] + gamma * v[s2])
                for p, s2 in transiciones[(s, a)]
            )
            if valor > mejor_valor:
                mejor_valor = valor
                mejor_accion = a
        politica[s] = mejor_accion
    return politica


def iteracion_politicas(estados, acciones, transiciones, recompensas):
    politica = {s: acciones[s][0] for s in estados}

    while True:
        v = evaluar_politica(estados, politica, transiciones, recompensas)
        nueva = mejorar_politica(estados, acciones, transiciones, recompensas, v)
        if nueva == politica:
            return politica, v
        politica = nueva


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

    politica, valores = iteracion_politicas(estados, acciones, transiciones, recompensas)
    print("Política óptima:", politica)
    print("Valores:", valores)

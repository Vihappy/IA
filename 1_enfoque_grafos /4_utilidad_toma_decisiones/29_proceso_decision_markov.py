def simular_mdp(estado_inicial, politica, transicion_determinista, recompensa, pasos=5):
    """Simulación simple de un MDP determinista."""
    estado = estado_inicial
    total = 0
    trayectoria = [estado]

    for _ in range(pasos):
        accion = politica[estado]
        siguiente = transicion_determinista[(estado, accion)]
        total += recompensa[(estado, accion, siguiente)]
        estado = siguiente
        trayectoria.append(estado)

    return trayectoria, total


if __name__ == "__main__":
    politica = {"S1": "mover", "S2": "quedarse"}
    transicion = {
        ("S1", "mover"): "S2",
        ("S2", "quedarse"): "S2",
    }
    recompensa = {
        ("S1", "mover", "S2"): 10,
        ("S2", "quedarse", "S2"): 1,
    }

    trayectoria, total = simular_mdp("S1", politica, transicion, recompensa, pasos=4)
    print("Trayectoria:", trayectoria)
    print("Recompensa total:", total)

import random


def contar_conflictos(var, valor, asignacion, vecinos):
    return sum(1 for n in vecinos[var] if asignacion.get(n) == valor)


def minimos_conflictos(variables, dominios, vecinos, max_pasos=1000):
    """Algoritmo Min-Conflicts para CSP."""
    asignacion = {v: random.choice(dominios[v]) for v in variables}

    for _ in range(max_pasos):
        en_conflicto = [
            v for v in variables if contar_conflictos(v, asignacion[v], asignacion, vecinos) > 0
        ]

        if not en_conflicto:
            return asignacion

        var = random.choice(en_conflicto)
        mejor_valor = min(dominios[var], key=lambda val: contar_conflictos(var, val, asignacion, vecinos))
        asignacion[var] = mejor_valor

    return None


if __name__ == "__main__":
    random.seed(3)

    variables = ["A", "B", "C", "D"]
    dominios = {v: [1, 2, 3] for v in variables}
    vecinos = {
        "A": ["B", "C"],
        "B": ["A", "C", "D"],
        "C": ["A", "B", "D"],
        "D": ["B", "C"],
    }

    print("Solución Min-Conflicts:", minimos_conflictos(variables, dominios, vecinos))

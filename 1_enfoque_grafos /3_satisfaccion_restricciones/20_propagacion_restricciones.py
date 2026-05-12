from collections import deque


def ac3(variables, dominios, vecinos):
    """AC-3 para restricciones de desigualdad X != Y."""
    cola = deque((x, y) for x in variables for y in vecinos[x])

    while cola:
        x, y = cola.popleft()
        if revisar_arco(x, y, dominios):
            if not dominios[x]:
                return False
            for z in vecinos[x]:
                if z != y:
                    cola.append((z, x))

    return True


def revisar_arco(x, y, dominios):
    revisado = False
    for vx in dominios[x][:]:
        # Debe existir algún vy distinto de vx
        if not any(vx != vy for vy in dominios[y]):
            dominios[x].remove(vx)
            revisado = True
    return revisado


if __name__ == "__main__":
    variables = ["A", "B", "C"]
    dominios = {
        "A": [1, 2],
        "B": [2],
        "C": [1, 2],
    }
    vecinos = {
        "A": ["B", "C"],
        "B": ["A"],
        "C": ["A"],
    }

    consistente = ac3(variables, dominios, vecinos)
    print("Consistente:", consistente)
    print("Dominios propagados:", dominios)

def forward_check(var, valor, dominios, vecinos, asignacion):
    """Elimina valores incompatibles en vecinos no asignados."""
    podados = []
    for vecino in vecinos[var]:
        if vecino in asignacion:
            continue

        for v in dominios[vecino][:]:
            if v == valor:
                dominios[vecino].remove(v)
                podados.append((vecino, v))

        if not dominios[vecino]:
            return False, podados

    return True, podados


def restaurar(dominios, podados):
    for var, valor in podados:
        if valor not in dominios[var]:
            dominios[var].append(valor)


def backtracking_forward(variables, dominios, vecinos, asignacion=None):
    if asignacion is None:
        asignacion = {}

    if len(asignacion) == len(variables):
        return asignacion

    var = next(v for v in variables if v not in asignacion)

    for valor in dominios[var][:]:
        # Consistencia local con vecinos ya asignados
        if any(asignacion.get(n) == valor for n in vecinos[var] if n in asignacion):
            continue

        asignacion[var] = valor
        ok, podados = forward_check(var, valor, dominios, vecinos, asignacion)

        if ok:
            resultado = backtracking_forward(variables, dominios, vecinos, asignacion)
            if resultado is not None:
                return resultado

        restaurar(dominios, podados)
        del asignacion[var]

    return None


if __name__ == "__main__":
    variables = ["A", "B", "C", "D"]
    dominios = {v: [1, 2, 3] for v in variables}
    vecinos = {
        "A": ["B", "C"],
        "B": ["A", "D"],
        "C": ["A", "D"],
        "D": ["B", "C"],
    }

    print("Solución FC:", backtracking_forward(variables, dominios, vecinos))

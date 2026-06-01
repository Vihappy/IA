def es_seguro(asignacion, var, valor, vecinos):
    for vecino in vecinos[var]:
        if vecino in asignacion and asignacion[vecino] == valor:
            return False
    return True


def vuelta_atras(variables, dominios, vecinos, asignacion=None):
    """Backtracking clásico para coloreo de grafos."""
    if asignacion is None:
        asignacion = {}

    if len(asignacion) == len(variables):
        return asignacion

    var = next(v for v in variables if v not in asignacion)

    for valor in dominios[var]:
        if es_seguro(asignacion, var, valor, vecinos):
            asignacion[var] = valor
            resultado = vuelta_atras(variables, dominios, vecinos, asignacion)
            if resultado is not None:
                return resultado
            del asignacion[var]

    return None


if __name__ == "__main__":
    variables = ["WA", "NT", "SA", "Q"]
    colores = ["Rojo", "Verde", "Azul"]
    dominios = {v: colores[:] for v in variables}
    vecinos = {
        "WA": ["NT", "SA"],
        "NT": ["WA", "SA", "Q"],
        "SA": ["WA", "NT", "Q"],
        "Q": ["NT", "SA"],
    }

    print("Asignación:", vuelta_atras(variables, dominios, vecinos))

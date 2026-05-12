def es_consistente(asignacion, restricciones):
    """Verifica restricciones binarias sobre pares (X, Y)."""
    for x, y, regla in restricciones:
        if x in asignacion and y in asignacion:
            if not regla(asignacion[x], asignacion[y]):
                return False
    return True


def resolver_csp_basico(variables, dominios, restricciones, asignacion=None):
    """Solver mínimo de CSP por backtracking."""
    if asignacion is None:
        asignacion = {}

    if len(asignacion) == len(variables):
        return asignacion

    var = next(v for v in variables if v not in asignacion)

    for valor in dominios[var]:
        nueva = dict(asignacion)
        nueva[var] = valor
        if es_consistente(nueva, restricciones):
            solucion = resolver_csp_basico(variables, dominios, restricciones, nueva)
            if solucion is not None:
                return solucion

    return None


if __name__ == "__main__":
    variables = ["A", "B", "C"]
    dominios = {v: [1, 2, 3] for v in variables}
    restricciones = [
        ("A", "B", lambda a, b: a != b),
        ("B", "C", lambda b, c: b != c),
    ]

    print("Solución CSP:", resolver_csp_basico(variables, dominios, restricciones))

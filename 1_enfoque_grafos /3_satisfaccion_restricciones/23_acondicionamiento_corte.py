from itertools import product


def consistente_parcial(asignacion, vecinos):
    for x, valor_x in asignacion.items():
        for y in vecinos[x]:
            if y in asignacion and asignacion[y] == valor_x:
                return False
    return True


def resolver_arbol(variables, dominios, vecinos, asignacion_base):
    """Backtracking simple sobre la parte restante (idealmente acíclica)."""
    asignacion = dict(asignacion_base)

    def bt():
        if len(asignacion) == len(variables):
            return True

        var = next(v for v in variables if v not in asignacion)
        for valor in dominios[var]:
            asignacion[var] = valor
            if consistente_parcial(asignacion, vecinos) and bt():
                return True
            del asignacion[var]
        return False

    return asignacion if bt() else None


def cutset_conditioning(variables, dominios, vecinos, cutset):
    """
    1) Prueba todas las asignaciones del cutset.
    2) Resuelve el resto con backtracking.
    """
    restantes = [v for v in variables if v not in cutset]

    for valores in product(*[dominios[v] for v in cutset]):
        asignacion_cutset = dict(zip(cutset, valores))
        if not consistente_parcial(asignacion_cutset, vecinos):
            continue

        solucion = resolver_arbol(restantes, dominios, vecinos, asignacion_cutset)
        if solucion is not None:
            return solucion

    return None


if __name__ == "__main__":
    variables = ["A", "B", "C", "D", "E"]
    dominios = {v: [1, 2, 3] for v in variables}
    vecinos = {
        "A": ["B", "C"],
        "B": ["A", "C", "D"],
        "C": ["A", "B", "E"],
        "D": ["B"],
        "E": ["C"],
    }

    # Quitar B y C rompe el ciclo principal
    cutset = ["B", "C"]
    print("Solución por cutset conditioning:", cutset_conditioning(variables, dominios, vecinos, cutset))

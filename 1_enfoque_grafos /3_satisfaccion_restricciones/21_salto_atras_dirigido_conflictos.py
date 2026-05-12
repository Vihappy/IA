def backjumping(variables, dominios, vecinos):
    """
    Versión compacta de Conflict-Directed Backjumping para coloreo.
    Retorna asignación o None.
    """
    asignacion = {}

    def resolver(i):
        if i == len(variables):
            return True, set()

        var = variables[i]
        conflictos_locales = set()

        for valor in dominios[var]:
            conflicto = None
            for vecino in vecinos[var]:
                if vecino in asignacion and asignacion[vecino] == valor:
                    conflicto = vecino
                    break

            if conflicto is None:
                asignacion[var] = valor
                ok, conjunto_conflicto = resolver(i + 1)
                if ok:
                    return True, set()

                if var not in conjunto_conflicto:
                    del asignacion[var]
                    return False, conjunto_conflicto

                conjunto_conflicto.discard(var)
                conflictos_locales |= conjunto_conflicto
                del asignacion[var]
            else:
                conflictos_locales.add(conflicto)

        conflictos_locales.add(var)
        return False, conflictos_locales

    ok, _ = resolver(0)
    return asignacion if ok else None


if __name__ == "__main__":
    variables = ["A", "B", "C", "D"]
    dominios = {v: [1, 2, 3] for v in variables}
    vecinos = {
        "A": ["B", "C"],
        "B": ["A", "C", "D"],
        "C": ["A", "B", "D"],
        "D": ["B", "C"],
    }

    print("Solución CBJ:", backjumping(variables, dominios, vecinos))

def utilidad_lineal(riqueza):
    return riqueza


def utilidad_concava(riqueza):
    # Modela aversión al riesgo
    return riqueza ** 0.5


def utilidad_esperada(resultados, utilidad_fn):
    """resultados: lista de (probabilidad, recompensa)."""
    return sum(p * utilidad_fn(r) for p, r in resultados)


if __name__ == "__main__":
    loteria = [(0.5, 100), (0.5, 0)]
    seguro = [(1.0, 45)]

    print("UE lotería (lineal):", utilidad_esperada(loteria, utilidad_lineal))
    print("UE seguro (lineal):", utilidad_esperada(seguro, utilidad_lineal))

    print("UE lotería (cóncava):", round(utilidad_esperada(loteria, utilidad_concava), 2))
    print("UE seguro (cóncava):", round(utilidad_esperada(seguro, utilidad_concava), 2))

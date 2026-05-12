def evaluar_politica_pasiva(episodios, gamma=0.9):
    """
    Estimación de V(s) en aprendizaje pasivo (política fija)
    usando retornos promedio por estado.
    episodios: lista de episodios, cada episodio es [(s, r), ...]
    """
    retornos = {}

    for episodio in episodios:
        g = 0
        visitado = set()
        for t in range(len(episodio) - 1, -1, -1):
            s, r = episodio[t]
            g = r + gamma * g
            if s not in visitado:  # first-visit MC
                retornos.setdefault(s, []).append(g)
                visitado.add(s)

    v = {s: sum(vals) / len(vals) for s, vals in retornos.items()}
    return v


if __name__ == "__main__":
    episodios = [
        [("S1", 0), ("S2", 1), ("S3", 5)],
        [("S1", 0), ("S2", 2), ("S3", 5)],
    ]

    print("Valores estimados:", evaluar_politica_pasiva(episodios))

def filtrar_hmm(prior, observaciones, p_trans, p_obs):
    """
    Filtro hacia delante para una DBN de 1 variable oculta (HMM).
    estados = {"Sano", "Enfermo"}
    """
    creencia = dict(prior)

    for obs in observaciones:
        pred = {}
        for s in creencia:
            pred[s] = sum(creencia[s0] * p_trans[(s0, s)] for s0 in creencia)

        nueva = {}
        z = 0
        for s in pred:
            nueva[s] = pred[s] * p_obs[(s, obs)]
            z += nueva[s]

        for s in nueva:
            nueva[s] /= z

        creencia = nueva

    return creencia


if __name__ == "__main__":
    prior = {"Sano": 0.7, "Enfermo": 0.3}
    p_trans = {
        ("Sano", "Sano"): 0.8,
        ("Sano", "Enfermo"): 0.2,
        ("Enfermo", "Sano"): 0.3,
        ("Enfermo", "Enfermo"): 0.7,
    }
    p_obs = {
        ("Sano", "fiebre"): 0.1,
        ("Enfermo", "fiebre"): 0.8,
    }

    posterior = filtrar_hmm(prior, ["fiebre", "fiebre"], p_trans, p_obs)
    print("Creencia final:", posterior)

def mejor_decision(prob_lluvia):
    """
    Mini red de decisión:
    - Decisión: llevar paraguas o no
    - Azar: llueve / no llueve
    - Utilidad según combinación
    """
    utilidades = {
        "paraguas": {"llueve": 8, "no_llueve": 5},
        "sin_paraguas": {"llueve": -10, "no_llueve": 10},
    }

    ue_paraguas = (
        prob_lluvia * utilidades["paraguas"]["llueve"]
        + (1 - prob_lluvia) * utilidades["paraguas"]["no_llueve"]
    )

    ue_sin = (
        prob_lluvia * utilidades["sin_paraguas"]["llueve"]
        + (1 - prob_lluvia) * utilidades["sin_paraguas"]["no_llueve"]
    )

    return ("paraguas", ue_paraguas) if ue_paraguas >= ue_sin else ("sin_paraguas", ue_sin)


if __name__ == "__main__":
    decision, ue = mejor_decision(prob_lluvia=0.4)
    print("Mejor decisión:", decision)
    print("Utilidad esperada:", ue)

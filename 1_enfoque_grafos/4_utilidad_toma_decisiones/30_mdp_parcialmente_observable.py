def actualizar_creencia(creencia, observacion, modelo_obs):
    """
    Actualiza creencia en un POMDP simplificado sin transición.
    creencia: dict estado->prob
    modelo_obs: dict (estado, observacion)->prob
    """
    nueva = {}
    normalizador = 0

    for estado, p in creencia.items():
        verosimilitud = modelo_obs[(estado, observacion)]
        nueva[estado] = p * verosimilitud
        normalizador += nueva[estado]

    for estado in nueva:
        nueva[estado] /= normalizador

    return nueva


def accion_por_creencia(creencia):
    # Si prob de lluvia alta, llevar paraguas
    return "paraguas" if creencia["lluvia"] > 0.5 else "sin_paraguas"


if __name__ == "__main__":
    creencia = {"lluvia": 0.4, "no_lluvia": 0.6}
    modelo_obs = {
        ("lluvia", "nubes"): 0.8,
        ("no_lluvia", "nubes"): 0.3,
    }

    creencia = actualizar_creencia(creencia, "nubes", modelo_obs)
    print("Nueva creencia:", creencia)
    print("Acción recomendada:", accion_por_creencia(creencia))

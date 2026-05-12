def valor_esperado_sin_informacion(prob_enfermo, utilidad_tratar_si, utilidad_no_tratar_si):
    # Mejor acción fija sin observar nada
    ue_tratar = prob_enfermo * utilidad_tratar_si[0] + (1 - prob_enfermo) * utilidad_tratar_si[1]
    ue_no = prob_enfermo * utilidad_no_tratar_si[0] + (1 - prob_enfermo) * utilidad_no_tratar_si[1]
    return max(ue_tratar, ue_no)


def valor_esperado_con_informacion_perfecta(prob_enfermo, utilidad_tratar_si, utilidad_no_tratar_si):
    # Con información perfecta, eliges la mejor acción por estado real
    mejor_si_enfermo = max(utilidad_tratar_si[0], utilidad_no_tratar_si[0])
    mejor_si_sano = max(utilidad_tratar_si[1], utilidad_no_tratar_si[1])
    return prob_enfermo * mejor_si_enfermo + (1 - prob_enfermo) * mejor_si_sano


if __name__ == "__main__":
    prob = 0.3
    # (utilidad si enfermo, utilidad si sano)
    tratar = (50, -10)
    no_tratar = (-40, 20)

    sin_info = valor_esperado_sin_informacion(prob, tratar, no_tratar)
    con_info = valor_esperado_con_informacion_perfecta(prob, tratar, no_tratar)

    print("VE sin información:", sin_info)
    print("VE con info perfecta:", con_info)
    print("Valor de la información:", con_info - sin_info)

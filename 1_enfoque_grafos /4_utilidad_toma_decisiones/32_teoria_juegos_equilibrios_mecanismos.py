def equilibrios_nash_puros(payoffs_fila, payoffs_col):
    """
    Busca equilibrios de Nash puros en juego 2x2.
    payoffs_fila[i][j], payoffs_col[i][j]
    """
    eq = []

    for i in range(2):
        for j in range(2):
            mejor_fila = payoffs_fila[i][j] >= payoffs_fila[1 - i][j]
            mejor_col = payoffs_col[i][j] >= payoffs_col[i][1 - j]
            if mejor_fila and mejor_col:
                eq.append((i, j))

    return eq


def subasta_segundo_precio(ofertas):
    """Mecanismo simple tipo Vickrey."""
    ordenadas = sorted(ofertas, key=lambda x: x[1], reverse=True)
    ganador = ordenadas[0][0]
    pago = ordenadas[1][1] if len(ordenadas) > 1 else 0
    return ganador, pago


if __name__ == "__main__":
    fila = [[3, 0], [5, 1]]
    col = [[3, 5], [0, 1]]
    print("Equilibrios Nash puros (índices):", equilibrios_nash_puros(fila, col))

    ofertas = [("Ana", 10), ("Luis", 8), ("Marta", 7)]
    print("Subasta 2do precio:", subasta_segundo_precio(ofertas))

def ordenar_ascendente(n1, n2, n3):
    # Ordena tres valores de menor a mayor mediante comparaciones directas
    if n1 > n2:
        n1, n2 = n2, n1
    if n2 > n3:
        n2, n3 = n3, n2
    if n1 > n2:
        n1, n2 = n2, n1
    return n1, n2, n3


if __name__ == "__main__":
    print(ordenar_ascendente(7, 2, 5))
    print(ordenar_ascendente(2, 2, 9))
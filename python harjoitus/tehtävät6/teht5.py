def poista_parittomat(lukulista):
    parilliset = []

    for luku in lukulista:
        if luku % 2 == 0:
            parilliset.append(luku)

    return parilliset

alkuperainen_lista = [1, 2, 3, 4, 5, 6, 7, 8]

karsittu_lista = poista_parittomat(alkuperainen_lista)

print("Alkuperäinen lista:", alkuperainen_lista)
print("Karsittu lista:", karsittu_lista)
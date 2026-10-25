arvot = []

while True:
    arvo = int(input("Anna arvo (0 lopettaa): "))

    if arvo == 0:
        break

    arvot.append(arvo)

    print("Lisäysjärjestyksessä:", arvot)
    print("Pienimmästä suurimpaan:", sorted(arvot))
from math import sqrt

while True:
    luku = int(input("Anna kokonaisluku: "))

    if luku == 0:
        print("Ohjelma lopetettu.")
        break
    elif luku < 0:
        print("Virheellinen numero!")
    else:
        neliojuuri = sqrt(luku)
        print(f"Luvun neliöjuuri on {neliojuuri}.")
tuotteet = []
maarat = []

while True:
    tuote = input("Mitä tuotetta valmistetaan? ")
    maara = int(input("Kuinka monta valmistetaan? "))

    tuotteet.append(tuote)
    maarat.append(maara)

    jatketaanko = input("Jatketaanko tuotantoa? ")

    if jatketaanko.lower() == "ei":
        break

print()
print("Tuotanto lopetettu!")
print()
print("Valmistetut tuotteet:")

for i in range(len(tuotteet)):
    print(f"{tuotteet[i]}: {maarat[i]} kpl")
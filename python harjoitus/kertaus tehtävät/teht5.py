sanat = []

while True:
    sana = input("Anna sana lisättäväksi tarinaan: ")

    if sana.lower() == "loppu":
        break

    sanat.append(sana)

tarina = " ".join(sanat)
print(tarina)
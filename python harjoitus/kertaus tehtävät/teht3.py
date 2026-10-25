while True:
    print("Tuote valmistettu!")
    jatketaanko = input("Jatketaanko tuotantoa? ")

    if jatketaanko.lower() == "ei":
        print("Tuotanto lopetettu!")
        break
    
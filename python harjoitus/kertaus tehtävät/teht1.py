tuntipalkka = float(input("Anna tuntipalkka: "))
tunnit = float(input("Anna tehdyt tunnit: "))
viikonpaiva = input("Anna viikonpäivä: ")

if viikonpaiva.lower() == "sunnuntai":
    paivapalkka = tuntipalkka * tunnit * 2
else:
    paivapalkka = tuntipalkka * tunnit

print(f"Päiväpalkka on {paivapalkka:.2f} euroa.")
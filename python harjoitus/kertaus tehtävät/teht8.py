kustannukset = [12.5, 8.2, 15.0, 6.5, 10.8]

yhteensa = 0

for kustannus in kustannukset:
    print(f"Tuotteen valmistuskustannus: {kustannus:.1f} €")
    yhteensa = yhteensa + kustannus

print()
print(f"Valmistuskustannukset yhteensä: {yhteensa:.1f} €")
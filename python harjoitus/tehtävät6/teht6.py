import math

def laske_yksikkohinta(halkaisija, hinta):
    sade_cm = halkaisija / 2
    sade_m = sade_cm / 100
    pinta_ala = math.pi * sade_m ** 2
    yksikkohinta = hinta / pinta_ala
    return yksikkohinta

halkaisija1 = float(input("Anna ensimmäisen pizzan halkaisija senttimetreinä: "))
hinta1 = float(input("Anna ensimmäisen pizzan hinta: "))

halkaisija2 = float(input("Anna toisen pizzan halkaisija senttimetreinä: "))
hinta2 = float(input("Anna toisen pizzan hinta: "))

yksikkohinta1 = laske_yksikkohinta(halkaisija1, hinta1)
yksikkohinta2 = laske_yksikkohinta(halkaisija2, hinta2)

print("Ensimmäisen pizzan yksikköhinta:", round(yksikkohinta1, 2), "euroa/m²")
print("Toisen pizzan yksikköhinta:", round(yksikkohinta2, 2), "euroa/m²")

if yksikkohinta1 < yksikkohinta2:
    print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
elif yksikkohinta2 < yksikkohinta1:
    print("Toinen pizza antaa paremman vastineen rahalle.")
else:
    print("Pizzoilla on sama yksikköhinta.")
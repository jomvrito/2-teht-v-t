def laske_summa(lukulista):
    summa = 0

    for luku in lukulista:
        summa = summa + luku

    return summa

luvut = [2, 5, 7, 10]

tulos = laske_summa(luvut)

print("Lukujen summa on:", tulos)
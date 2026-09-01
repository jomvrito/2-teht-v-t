leiviskat = float(input("anna leiviskät: "))

naulat = float(input("anna naulat: "))

luodit = float(input("anna luodit: "))


grammat = (leiviskat * 20 * 32 * 13.3) + (naulat * 32 * 13.3) + (luodit *13.3)

kilogrammat =int(grammat / 1000)

loput = grammat % 1000

print(f"massa nykymittojen mukaan on: {kilogrammat} kilogrammaa ja {loput:.2f} grammaa.")




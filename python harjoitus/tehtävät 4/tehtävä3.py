syote = input("anna luku (tyhjä lopettaa): ")
pienin = None
suurin = None
while syote != "":
    luku = float(syote)
    if pienin is None or luku < pienin:
        pienin = luku
    if suurin is None or luku > suurin:
        suurin = luku
    syote = input("anna luku (tyhjä lopettaa): ")        
if pienin is not None:
    print("pieninluku:", pienin)
    print("suurin luku", suurin)    
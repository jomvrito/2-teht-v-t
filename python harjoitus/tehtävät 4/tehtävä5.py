oikea_tunnus = "opiskelija"
oikea_salasana = "python123"
yritykset = 0
kirjautuminen_oikein = False
while yritykset < 5:
    tunnus = input("anna käyttäjätunnus: ")
    salasana = input("anna salasana: ")
    yritykset = yritykset + 1 
    if tunnus == oikea_tunnus and salasana == oikea_salasana:
        kirjautuminen_oikein = True
        break
if kirjautuminen_oikein:
    print("tervetuloa")
else:
    print("pääsy evätty")    
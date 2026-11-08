import random

def heita_noppaa(tahkot):
    silmaluku = random.randint(1, tahkot)
    return silmaluku

tahkot = int(input("Montako tahkoa nopassa on? "))

silmaluku = 0

while silmaluku != tahkot:
    silmaluku = heita_noppaa(tahkot)
    print(silmaluku)
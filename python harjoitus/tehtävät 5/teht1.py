import random

noppien_maara = int(input("anna arpakuutioiden lukumäärä: "))
summa = 0

for i in range(noppien_maara):
    silmaluku = random.randint(1, 6)
    summa = summa + silmaluku

print(f"silmälukujen summa on {summa}.")    

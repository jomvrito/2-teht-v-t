import random

def heita_noppaa():
    silmaluku = random.randint(1, 6)
    return silmaluku

silmaluku = 0

while silmaluku != 6:
    silmaluku = heita_noppaa()
    print(silmaluku)
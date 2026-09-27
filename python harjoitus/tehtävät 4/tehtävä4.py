import random
oikea_luku = random.randint(1, 10)
arvaus = int(input("arvaa luku väliltä 1-10: "))
while arvaus != oikea_luku:
    if arvaus > oikea_luku:
        print("liian suuri arvaus")
    else:
        print("liian ieni arvaus")
    arvaus = int(input("arvaa uudelleen: "))
print("oikein")    
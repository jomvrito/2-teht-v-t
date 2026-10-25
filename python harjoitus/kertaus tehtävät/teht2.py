luku = int(input("Anna kokonaisluku: "))

if luku % 3 == 0 and luku % 5 == 0:
    print("Jaollinen molemmilla luvuilla!")
elif luku % 3 == 0:
    print("Kolmella jaollinen")
elif luku % 5 == 0:
    print("Viidellä jaollinen")
else:
    print("Luku ei ole jaollinen kolmella eikä viidellä.")
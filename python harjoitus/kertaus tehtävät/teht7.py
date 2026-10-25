sanat = [
    "tuotanto",
    "kone",
    "varasto",
    "laatu",
    "kuljetus",
    "asiakas",
    "myynti"
]

maara = 0

for sana in sanat:
    if len(sana) > 5:
        maara = maara + 1

print(f"Listassa on {maara} sanaa, joissa on enemmän kuin 5 kirjainta.")
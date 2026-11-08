def gallonat_litroiksi(gallonat):
    litrat = gallonat * 3.785
    return litrat

gallonat = float(input("Anna gallonamäärä: "))

while gallonat >= 0:
    litrat = gallonat_litroiksi(gallonat)
    print("Litroina:", litrat)

    gallonat = float(input("Anna gallonamäärä: "))
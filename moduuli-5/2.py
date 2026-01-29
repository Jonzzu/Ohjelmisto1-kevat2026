luvut = []

while True:
    syote = input("Enter a number: ") # Kysytään numerot
    if syote == "":                 # tyhjä syöte lopettaa
        break
    else:
        luku = float(syote)   # muunnetaan syöte luvuksi
        luvut.append(luku)    # Lisätään numero listan loppuun

# Järjestetään lista laskevaan järjestykseen
luvut.sort(reverse=True)

# Tulostetaan viisi suurinta
print("The greatest numbers in descending order: ")
for luku in luvut[:5]:
    print(luku)


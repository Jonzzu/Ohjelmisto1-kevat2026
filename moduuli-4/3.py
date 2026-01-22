pienin = None
suurin = None

while True:
    syote = input("Enter a number (or press Enter to quit): ")
    if syote == "":
        break

    luku = float(syote)

    if pienin is None or luku < pienin:
        pienin = luku
    if suurin is None or luku > suurin:
        suurin = luku

if pienin is not None:
    print("Smallest number:", pienin)
    print("Largest number:", suurin)

import random

def roll_dice(tahkot):
    return random.randint(1,tahkot)

tahkot = int(input('Anna tahkojen määrä: '))
maksimisilmäluku = tahkot

while True:
    silmäluku = roll_dice(tahkot)
    print(f'{silmäluku}')
    if silmäluku == maksimisilmäluku:
        break
import random

def roll_dice():
    return random.randint(1, 6)

while True:
    luku = roll_dice()
    print(f'{luku}')
    if luku == 6:
        break
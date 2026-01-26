import random
noppa = int(input('How many dice to roll: '))
summa = 0
for n in range(noppa):
    heitto = random.randint(1,6)
    summa = summa + heitto
print(f'Sum of the dice: {summa}')
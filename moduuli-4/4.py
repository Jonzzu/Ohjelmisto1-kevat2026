import random
random_number = random.randint(1, 10)
while True:
    number_inputted = int(input('Guess a number 1-10:'))
    if number_inputted == random_number:
        print('Correct')
        break
    if number_inputted < random_number:
        print('Too low')
    if number_inputted > random_number:
        print('Too high')

kaupungit = []

for kaupunki in range(5):
    kaupunki = input('Enter the name of a city: ')
    kaupungit.append(kaupunki)

print('\n\nThe cities you entered: ')

for kaupunki in kaupungit:
    print(f'{kaupunki}')
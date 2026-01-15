talents = float(input('Enter talents:'))
pounds = float(input('Enter pounds:'))
lots = float(input('Enter lots:'))

lots_to_grams = lots * 13,3
pounds_to_lots = pounds * 32
talents_to_pounds = talents * 20

total_grams = talents_to_pounds + pounds_to_lots + lots_to_grams
kilograms = total_grams / 1000
remaining_grams =
print('The weight in modern units:')
print(f'{kilograms} kilograms and {total_grams} grams.')
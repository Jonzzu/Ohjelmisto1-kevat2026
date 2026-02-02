import math
def calculate_unit_price(cm, euros):
    radius = cm / 2
    area_cm2 = math.pi * radius ** 2
    area_m2 = area_cm2 / 10000
    unit_price = euros / area_m2
    return unit_price

diameter_1 = float(input('Enter the diameter of the first pizza (cm): '))
price_1 = float(input('Enter the price of the first pizza (euros): '))
diameter_2 = float(input('Enter the diameter of the second pizza (cm): '))
price_2 = float(input('Enter the price of the second pizza (euros): '))

unit_price1 = calculate_unit_price(diameter_1, price_1)
unit_price2 = calculate_unit_price(diameter_2, price_2)
print(f'Unit price of the first pizza: {unit_price1:.2f} euros/m\u00b2')
print(f'Unit price of the second pizza: {unit_price2:.2f} euros/m\u00b2')
if unit_price1 < unit_price2:
    print('The first pizza provides better value for money.')
if unit_price1 > unit_price2:
    print('The second pizza provides better value for money.')
if unit_price1 == unit_price2:
    print('The pizzas are of equal value.')
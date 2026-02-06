def get_season(m):
    if m in [12, 1, 2]:
        return 'winter'
    elif m in [3, 4, 5]:
        return 'spring'
    elif m in [6, 7, 8]:
        return 'summer'
    elif m in [9, 10, 11]:
        return 'autumn'
    else:
        return 0

m = int(input('Enter the number of a month (1-12): '))

print(f'You entered: {m}')

if m < 1 or m > 12:
    print('Please enter a number between 1 and 12.')
else:
    season = get_season(m)
    print(f'The season is {season}.')

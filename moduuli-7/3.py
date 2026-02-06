airports = {}

loop1 = 0
while loop1 != 3:
    print('')
    print('Airport Data Management')
    print('1. Enter a new airport')
    print('2. Fetch airport information')
    print('3. Quit')
    loop1 = int(input('Please choose an option (1-3): '))
    if loop1 == 1:
        icao = input('Enter the ICAO code: ')
        airport = input('Enter the airport name: ')
        airports[icao] = airport
        print(f'Airport {airport} with ICAO code {icao} has been added.')

    elif loop1 == 2:
        icao = input('Enter the ICAO code: ')
        if icao in airports:
            print(f'The airport with ICAO code {icao} is {airports[icao]}.')
        else:
            print(f'No airport found with ICAO code {icao}.')

    else:
        print('Thank you for using the Airport Data Management system. Goodbye!')
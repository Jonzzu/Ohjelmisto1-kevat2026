import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='Jonne',
    password='salasana',
    autocommit=True
)


def get_airport_coordinates(icao_code):

    sql = """ SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s; """
    kursori = yhteys.cursor()
    kursori.execute(sql, (icao_code,))
    tulos = kursori.fetchall()

    if not tulos:
        return None
    else:
        return tulos

#print(get_airport_coordinates(icao_code=input('Enter ICAO code: ').upper()))

def run_airport_distance():
    country_code1 = input('Enter the ICAO code of the first airport: ').upper()
    coordinates1 = get_airport_coordinates(country_code1)
    country_code2 = input('Enter the ICAO code of the second airport: ').upper()
    coordinates2 = get_airport_coordinates(country_code2)

    if coordinates1 is None or coordinates2 is None:
        print(f'Invalid ICAO code entered. You entered {country_code1} and {country_code2}')
    else:
        from geopy.distance import geodesic
        country1 = coordinates1
        country2 = coordinates2
        distance = geodesic(country1, country2).km
        print(f'Distance between {country_code1} and {country_code2}: {distance:.2f} kilometers')

run_airport_distance()
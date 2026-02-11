import mysql.connector

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='Jonne',
    password='salasana',
    autocommit=True
)

def get_airports_by_country(country_code):
    sql =   """
            SELECT type, count(*)
            FROM airport
            WHERE iso_country = %s
            GROUP BY type
            ORDER BY FIELD(type,'small_airport', 'medium_airport', 'heliport', 'large_airport');
"""

    kursori = yhteys.cursor()
    kursori.execute(sql, (country_code,))
    tulos = kursori.fetchall()
    if not tulos:
        return None
    else:
        return tulos

def run_country_program():
    country_code = input('Enter the country code (e.g., FI for Finland): ').upper()
    airports_in_country = get_airports_by_country(country_code)

    if airports_in_country is None:
        print(f"No airports found for country code '{country_code}'.")
    else:
        print(f'\n\nAirports in {country_code}:')
        for tyyppi, maara in airports_in_country:
            print(maara, tyyppi, 'airports')

run_country_program()
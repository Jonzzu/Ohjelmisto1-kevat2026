import mysql.connector

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='Jonne',
         password='salasana',
         autocommit=True
         )

def hae_icao(ICAO):
    sql = f"SELECT airport.name AS 'Airport', airport.municipality AS 'Location' FROM airport WHERE airport.ident = '{ICAO}';"

    kursori = yhteys.cursor()
    kursori.execute(sql)

    tulos = kursori.fetchall()
    if not tulos:
        return None
    else:
        return tulos

ICAO = input('Enter ICAO: ').upper()
tulos = hae_icao(ICAO)

if tulos is None:
    print(f'No airport found with ICAO code {ICAO}')

else:
    (airport, location) = tulos[0]
    print(f'Airport name: {airport}\nLocation: {location}')
# Write a program that asks the user to enter the ICAO codes of two airports. The program prints out the
#  distance between the two airports in kilometers. The calculation is based on the airport coordinates fetched
#  from the database. Calculate the distance using the geopy library: https://geopy.readthedocs.io/en/stable/.
#  Install the library by selecting View / Tool Windows / Python Packages in your PyCharm IDE, write geopy into
#  the search field and finish the installation.


import mariadb
import sys
from geopy.distance import geodesic

def get_coordinates(icao_code, cursor):
    query = """
        SELECT latitude_deg, longitude_deg
        FROM airports
        WHERE ident = ?
    """
    cursor.execute(query, (icao_code,))
    result = cursor.fetchone()

    if result is None:
        return None
    
    return (result[0], result[1])


def main():

    config = {
        "host": "127.0.0.1",
        "port": 3306,
        "user": "root",
        "password": "Shirish.@1",
        "database": "airport"
    }

    icao1 = input("Enter first ICAO code: ").upper()
    icao2 = input("Enter second ICAO code: ").upper()

    try:
        conn = mariadb.connect(**config)
        print("Database connected")
        cursor = conn.cursor()

        coord1 = get_coordinates(icao1, cursor)
        coord2 = get_coordinates(icao2, cursor)

        if coord1 is None:
            print(f"Airport {icao1} not found.")
            return
        
        if coord2 is None:
            print(f"Airport {icao2} not found.")
            return

        distance = geodesic(coord1, coord2).kilometers

        print(f"The distance between {icao1} and {icao2} is {distance:.2f} km.")

    except mariadb.Error as e:
        print(f"Database error: {e}")
        sys.exit(1)

    finally:
        if 'conn' in locals():
            conn.close()


main()



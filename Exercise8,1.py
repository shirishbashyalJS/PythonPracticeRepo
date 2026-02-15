# Write a program that asks the user to enter the ICAO code of an airport. The program fetches and prints out
#  the corresponding airport name and location (town) from the airport database used on this course. The ICAO
#  codes are stored in the ident column of the airport table.


import mariadb
import sys



def database(ICAO_code):
    # Configuration dictionary for cleaner code
    config = {
        "host": "127.0.0.1",
        "port": 3306,
        "user": "root",
        "password": "Shirish.@1",
        "database": "airport"
    }

    try:
        # Establish the connection
        conn = mariadb.connect(**config)
        print("Successfully connected to MariaDB!")

        # Create a cursor to execute queries
        cur = conn.cursor()
        query = "SELECT name, municipality FROM airports WHERE ident=?"
        # Example: Fetching data
        cur.execute(query,(ICAO_code,))
        
        results = cur.fetchall()
        if results:
            for (name, municipality) in results:
                print(f"\nAirport Found!")
                print(f"Name: {name}")
                print(f"Location: {municipality}")
        else:
            print(f"\nNo airport found with ICAO code: {ICAO_code}")
    except mariadb.Error as e:
        print(f"Error connecting to MariaDB: {e}")
        sys.exit(1)

    finally:
        # Always close the connection when done
        if 'conn' in locals():
            conn.close()




def main():

    ICAO_Code = input("Enter ICAO code of an airport: ")
    database(ICAO_Code)




main()
# Write a program that asks the user to enter the area code (for example FI) and prints out the airports located
#  in that country ordered by airport type. For example, Finland has 65 small airports, 15 helicopter airports 
# and so on.


import mariadb
import sys

def database(area_code):
    
    config = {
        "host": "127.0.0.1",
        "port": 3306,
        "user":"root",
        "password":"Shirish.@1",
        "database":"airport"
    }

    try:
        conn = mariadb.connect(**config)
        print("Database connected")
        cur = conn.cursor()
        query =  """
            SELECT type, COUNT(*)
            FROM airports
            WHERE iso_country=?
            GROUP BY type
            ORDER BY type
            """


        cur.execute(query, (area_code,))

        results = cur.fetchall()
        

        print(f"{area_code} has ", end="")

        for index, (airport_type, count) in enumerate(results):

            name = airport_type.replace("_", " ")
            if count > 1:
                name += "s"

            if index == len(results) - 1:
                print(f"and {count} {name}.")
            else:
                print(f"{count} {name}, ", end="")

            

    except mariadb.Error as e:
        print(f"Error connecting to MariaDB: {e}")
        sys.exit(1)
    
    finally:
        # Always close the connection when done
        if 'conn' in locals():
            conn.close()


def main():
    area_code = input("Enter the area code (Eg FI for Finland): ")
    database(area_code)


main()
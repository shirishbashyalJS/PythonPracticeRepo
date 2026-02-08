# Write a program for fetching and storing airport data. The program asks the user if they want to enter a new airport, fetch the information of an existing airport or quit. If the user chooses to enter a new airport, the program asks the user to enter the ICAO code and name of the airport. If the user chooses to fetch airport information instead, the program asks for the ICAO code of the airport and prints out the corresponding name. If the user chooses to quit, the program execution ends. The user can choose a new option as many times they want until they choose to quit. (The ICAO code is an identifier that is unique to each airport. For example, the ICAO code of Helsinki-Vantaa Airport is EFHK. You can easily find the ICAO codes of different airports online.)



airports = {
    "EFHK": "Helsinki-Vantaa",
    "EFTU": "Turku Airport",
    "EFTP": "Tampere-Pirkkala",
    "EFOU": "Oulu Airport",
    "EFRO": "Rovaniemi Airport",
    "EFKU": "Kuopio Airport",
    "EFVA": "Vaasa Airport"
}

while True:
    decision = input("Enter a new airport, fetch the information of an existing airport or quit. Type 'new' for new airport, 'fetch' for fetching details and 'quit' for quiting: ").lower()
    if decision == "new":
        code=input("Enter the ICAO code of the airport: ").upper()
        name=input("Enter the name of the airport: ")
        
        if code in airports:
            print("Airport already exists.")
        else:
            airports[code] = name
            print("Airport successfully added.")

    elif decision == "fetch":
        code = input("Enter the ICAO code of the airport: ").upper()
        if code in airports:
            print(airports[code])
        else:
            print("Airport not found.")

    elif decision == "quit":
        print("Program Ended!")
        break
    else:
        print("Invalid option. Use: new, fetch, or quit.")




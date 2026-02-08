# Write a program that asks the user for a username and password. If either or both are incorrect, the program ask the user to enter the username and password again. This continues until the login information is correct or wrong credentials have been entered five times. If the information is correct, the program prints out Welcome. After five failed attempts the program prints out Access denied. The correct username is python and password rules.

username = "python"
password = "rules"

count = 1

while True:
    entered_username = input("Enter username: ")
    entered_password = input("Enter password: ")
    if(entered_username == username and entered_password == password):
        print("Welcome!")
        break
    elif(count >= 5):
        print("Access Denied!")
        break
    else:
        print(f"Wrong credentials. Please Enter Again, remaining attempts: ({5-count})")
    count+=1
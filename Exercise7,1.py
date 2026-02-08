# Write a program that asks the user for a number of a month and then prints out the corresponding season (spring, summer, autumn, winter). Save the seasons as strings into a tuple in your program. We can define each season to last three months, December being the first month of winter.


seasons= ( "winter","spring", "summer", "autumn")

month = int(input("Enter number (1 to 12) corresponding to months: "))

if month in [12,1,2]:
    print(seasons[0])
elif month in [3,4,5]:
    print(seasons[1])
elif month in [6,7,8]:
    print(seasons[2])
elif month in [9,10,11]:
    print(seasons[3])
else:
    print("Please enter valid month number(1-12).")


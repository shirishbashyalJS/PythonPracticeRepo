# Write a program that converts inches to centimeters until the user inputs a negative value. Then the program ends.

while True:
    inches = float(input("Enter inches for conversion to centimeter(use negative for ending): "))
    if(inches<0):
        break
    centimeter = 2.54 * inches
    print(f"{inches} inches is equal to {centimeter} centimeter.")
    
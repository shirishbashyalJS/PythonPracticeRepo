# Write a function that gets the quantity of gasoline in American gallons 
# and returns the number converted to litres. Write a main program that
#  asks for a volume in gallons from the user and converts the value to
#  liters. The conversion must be done by using the function. Conversions
#  continue until the user inputs a negative value.


def gallons_to_liter(gallons):
    return gallons * 3.7854


def main():
    print("NOTE: Use negative input for Exit!")
    while True:
        gallons = float(input("Enter the volume in gallons: "))
        if(gallons < 0):
            break

        liter = gallons_to_liter(gallons)
        print(f"{gallons} gallons is equal to {round(liter,2)} Liter.")
    
main()




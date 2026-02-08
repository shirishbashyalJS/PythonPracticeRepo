# Write a program that asks the user for three integer numbers. The program prints out the sum, product, and average of the numbers

def main():
    try:
        Number_one = int(input("Enter First Number: "))
        Number_two = int(input("Enter Second Number: "))
        Number_three = int(input("Enter Third Number: "))
    except ValueError:
        print("Please Enter Only Integer Value!")
        return

    sum = Number_one + Number_two + Number_three
    average = round((sum / 3), 2)
    product = Number_one * Number_two * Number_three

    print(f"The sum, average and product of given three number is: \n Sum: {sum} \n Average: {average} \n Product: {product}")

main()
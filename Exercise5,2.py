# Write a program that asks the user to enter numbers until they input an
#  empty string to quit. At the end, the program prints out the five
#  greatest numbers sorted in descending order. Hint: You can reverse
#  the order of sorted list items by using the sort method with the
#  reverse=True argument

numbers = []

while True:
    input_number= (input("Enter number: "))
    try:
        input_number = int(input_number)
        numbers.append(input_number)
    except ValueError:
        if(input_number == ""):
            break
        else:
            print("Enter only numbers!")
            continue

numbers.sort(reverse=True)
top_five = numbers[:5]
print(top_five)
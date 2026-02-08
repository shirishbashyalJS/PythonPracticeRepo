# Write a program that asks the user to enter numbers until they enter an empty string to quit. Finally, the program prints out the smallest and largest number from the numbers it received.
print("Just Enter empty for end of the program.")
count = 1
largest = None
smallest = None
while True:
    
    input_number = (input(f"{count}) Enter number: "))
    if(input_number == ""):
        break
    try:
        input_number = float(input_number)
    except ValueError:
        print("Enter valid datatype:")
        continue
    if(largest == None and smallest==None):
        largest = input_number
        smallest = input_number
    else:
        if(input_number>largest):
            largest = input_number
        if(input_number < smallest):
            smallest = input_number
    count+=1
    

if(largest == None):
    print("No any number have been entered!")
else:
    print(f"The largest number is {largest} and the smallest number is {smallest}")
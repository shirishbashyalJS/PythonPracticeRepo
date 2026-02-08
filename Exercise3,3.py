# Write a program that asks for the biological gender and hemoglobin value (g/l). The program the notifies the user if the hemoglobin value is low, normal or high.

# A normal hemoglobin value for adult females is between 117-155 g/l.
# A normal hemoglobin value for adult males is between 134-167 g/l.

gender = input("Enter the biological gender: ")
hemoglobin = float(input("Enter the hemoglobin value (g/l): "))

if(gender.lower() == "male"):
    if(hemoglobin > 167):
        print("You have high hemoglobin value.")
    elif(hemoglobin < 134):
        print("You have low hemoglobin value.")
    else:
        print("You have normal hemoglobin value.")
elif(gender.lower() == "female"):
    if(hemoglobin > 155):
        print("You have high hemoglobin value.")
    elif(hemoglobin < 117):
        print("You have low hemoglobin value.")
    else:
        print("You have normal hemoglobin value.")
else:
    print("Please enter valid gender(male/female)")

# Modify the function above so that it gets the number of sides on the dice as a parameter. With the modified function you can for example roll a 21-sided role-playing dice. The difference to the last exercise is that the dice rolling in the main program continues until the program gets the maximum number on the dice, which is asked from the user at the beginning.
import random

def dice_roller(number_of_sides):
    return random.randint(1,number_of_sides)



def main():
    number_of_sides = int(input("Enter the number of sides on dice: "))
    while True:
        rolled_number = dice_roller(number_of_sides)
        print(rolled_number)
        if(rolled_number == number_of_sides):
            break

main()
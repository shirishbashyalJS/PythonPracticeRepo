# Write a program that asks the user how many dice to roll.
#  The program rolls all the dice once and prints out the sum of the
#  numbers. Use a for loop.
import random

number_of_dice = int(input("Enter the number of dice to roll: "))
total = 0

for i in range(number_of_dice):
    total += random.randint(1,6)

print(f"The total of {number_of_dice} rolled dice is {total}")

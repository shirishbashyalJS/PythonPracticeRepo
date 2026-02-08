# Write a function that receives two parameters: the diameter of a round pizza in centimeters and the price of the pizza in euros. The function calculates and returns the unit price of the pizza per square meter. The main program asks the user to enter the diameter and price of two pizzas and tells the user which pizza provides better value for money (which of them has a lower unit price). You must use the function you wrote for calculating the unit prices.

import math

def cost_per_unit(diameter,price):
    area = math.pi * (diameter / 200 ) ** 2
    return price/area



def main():
    pizza1_diameter = float(input("Enter the diameter of pizza 1: "))
    pizza1_price = float(input("Enter the price of pizza 1: "))
    pizza2_diameter = float(input("Enter the diameter of pizza 2: "))
    pizza2_price = float(input("Enter the price of pizza 2: "))
    cost_per_unit_pizza_1 = cost_per_unit(pizza1_diameter,pizza1_price)
    cost_per_unit_pizza_2 = cost_per_unit(pizza2_diameter,pizza2_price)
    if(cost_per_unit_pizza_1<cost_per_unit_pizza_2):
        print(f"Pizza having diameter {pizza1_diameter} cm and rate {pizza1_price} provides better value for money")
    else:
        print(f"Pizza having diameter {pizza2_diameter} cm and rate {pizza2_price} provides better value for money")    



main()
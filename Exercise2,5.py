# Write a program that asks the user to enter a mass in medieval units: talents (leiviskä), pounds (naula), and lots (luoti). The program converts the input to full kilograms and grams and outputs the result to the user:

# One talent is 20 pounds.
# One pound is 32 lots.
# One lot is 13,3 grams.

talent = float(input("Enter talent: "))
pound = float(input("Enter pound: "))
lot = float(input("Enter lot: "))

lot = ((talent * 20 + pound ) * 32 + lot) * 13.3

kilogram = round(lot // 1000)
gram = round(lot % 1000)

print("The weight in mordern units:")
print(f"{kilogram} kilogram and {gram} grams")

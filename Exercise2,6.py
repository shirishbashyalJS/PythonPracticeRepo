# Write a program that draws two random combinations of numbers for a combination lock:
# a 3-digit code where each number is between 0 and 9.
# a 4-digit code where each number is between 1 and 6.

import random

Code_3_digit = random.randint(0,999)
code_4_digit = 0
for i in range(4):
    code_4_digit = random.randint(1,6) + code_4_digit*10

print(f"The 3-digit and 4-digit random combination is : {Code_3_digit} and {code_4_digit} respectively.")
# Write a game where the computer draws a random integer between 1 and 10. The user tries to guess the number until they guess the right number. After each guess the program prints out a text: Too high, Too low or Correct. Notice that the computer must not change the number between guesses.
import random
computer_guess = random.randint(1,10)

while True:
    user_guess = int(input("Guess the number from 1 to 10: "))
    if(user_guess<computer_guess):
        print("Too Low!")
    elif(user_guess>computer_guess):
        print("Too High!")
    else:
        print("Correct!")
        break
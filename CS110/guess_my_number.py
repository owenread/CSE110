"""
This is a game that tries to et a user to guess the correct number between 1-10
Author: Owen Read

"""
import random

play_again = "yes"

while play_again == "yes":
    number = random.randint(1, 100)
    #Remove following print at the end a coding
    print(number)
    guess = int(input("What number am I thinking of? "))
    guess_amount = 1

    while True:
        if guess < number:
            print("you should guess higher.")
            guess = int(input("What is your new guess? "))
            guess_amount += 1
        elif guess > number:
            print("You should guess lower.")
            guess = int(input("What is your new guess? "))
            guess_amount += 1
        else:
            print("You guessed correctly!")
            break
    if guess_amount == 1:
        print(f"It took you {guess_amount} time to guess correctly, that's amazing!")
    else:
        print(f"It took you {guess_amount} times to guess correctly.")
    
    play_again = input("Would you like to play again? yes/no: ").strip().lower()

print("Thanks for playing! Goodbye!")
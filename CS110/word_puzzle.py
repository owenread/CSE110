"""
I used Stack Overflow to help me figure out how to pull a random word out of my list.
I also added game instructions and made sure that the 'attempts' output was grammatically correct. 
I hope you enjoy!

Word guess puzzle

Author: Owen Read

"""
# Randomize the word that the user is trying to guess with a list. 
import random

word_options = ["clue", "pie", "turkey", "family", "nake", "puzzle", "train", "actor"]

word = random.choice(word_options)

# Welcome the user.
print("Welcome to the Word Puzzle!")
print("")
# Introduce the game instructions for the user. 
print("Here are the rules:\n" \
"1. Guess a word that has the same lengh as the spaces:'_' in the hint.\n" \
"2. If no letter from your guess is present, no space will be filled\n" \
"3. If a letter from your guess is present but in the incorrect location in the word,\n" \
"that letter will be displayed in lowercase in your hint\n" \
"4. If a letter from your guess is present in the word and in the correct location,\n" \
"that letter will be displayed in uppercase in your hint.")
print("good luck!")
print("")

# Print the hint and index the word.
print("Your first hint is:", end=" ")
for i in range(len(word)):
      print("_ ", end="")
print("")

# Define variables before the while loop

attempts = 0

guess = ""

while guess != word:
    guess = input("What is your guess? ").lower()
    attempts += 1
    print("")

    if len(guess) != len(word):
        print("The guess needs to be the same number of letters as the secret word!\n"
        "Try again!")
        print("")
        
# Add your guess is not correct after an incorrect guess
    else:

        if guess == word:
              break

        print("That's incorrect.")
        print("Your hint is:", end=" ")
        # Index the guess and the word to be able to compare
        for i in range(len(word)):
            word_letter = word[i]
            guess_letter = guess[i]
            # Prepare/Format the hints
            if word_letter == guess_letter:
                    print(guess_letter.upper(), end=" ")
            elif guess_letter in word:
                    print(guess_letter.lower(), end=" ")
            else:
                    print("_", end=" ")
        print("")
# Text that appears when user gets out of the loop
print("Congratulations! You guessed the word!")

# Tell the user how many attempts it took accounting for grammar. 
if attempts == 1:
      print(f"It took you {attempts} try! Look at you go!")
else:
        print(f"It took you {attempts} guesses.")
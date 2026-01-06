word = "Pizza"

print("Welcome to the word guessing game!\n")

# FIRST HINT USING A LOOP
print("Here is your hint:")
for _ in range(len(word)):
    print("_", end=" ")
print("\n")

attempts = 0
guess = ""

while guess != word:
    guess = input("What is your guess? ")
    attempts += 1

    # If guess is wrong length → warning only, loop continues
    if len(guess) != len(word):
        print("The guess needs to be the same number of letters as the secret word!\n")
        continue  # Go back to ask for guess again WITHOUT showing hint

    # Show hint when guess is the correct length
    print("Here is your hint:")
    for _ in range(len(word)):
        print("_", end=" ")
    print()

    # Letter-by-letter feedback
    for i in range(len(word)):
        word_letter = word[i]
        guess_letter = guess[i]

        if guess_letter == word_letter:
            print(guess_letter.upper(), end=" ")
        elif guess_letter in word:
            print(guess_letter.lower(), end=" ")
        else:
            print("_", end=" ")
    print("\n")

# Game ends when guess == word
print("Congratulations! You guessed it!")
print(f"It took you {attempts} guesses.")
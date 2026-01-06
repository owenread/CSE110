# Define the correct answer(s)
CORRECT_ANSWERS = ["answer1", "answer2", "answer3"] 

# Use a while loop to repeatedly ask until the answer is correct
while True:
    # Ask the riddle
    user_input = input("Riddle: What has keys but opens no locks? ")
    
    # Optional: Format the input (e.g., lowercase, remove leading/trailing spaces)
    user_input = user_input.strip().lower()

    # Check if the input is in the list of correct answers
    if user_input in CORRECT_ANSWERS:
        print("Correct! The door unlocks.")
        # Break the loop to continue with the rest of the game
        break 
    else:
        # Provide feedback and the loop restarts automatically
        print("Incorrect answer. Try again.")
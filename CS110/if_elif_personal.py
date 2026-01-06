def get_yes_no_input():
    
    while True:
        # Added creativity asking if they want to add a shake. 
        choice = input("Would you like to add a shake? (yes/no): ").lower()

        if choice == 'yes' or choice == 'y':
            shake_cost = input("How much does a shake cost? ")
            shake_quantity = input("How much many shakes? ")
            
            
            # You might loop back or return this value, depending on your needs.
            break # Exit the while loop if 'yes' was handled

        elif choice == 'no' or choice == 'n':
            print("--- User chose 'no', continuing with the program... ---")
            break # Exit the while loop and continue the program

        else:
            # If the input is not 'yes' or 'no', inform the user and loop again
            print("Invalid input. Please enter 'yes' or 'no'.")

# --- Rest of your program starts here ---
print("Program starting...")
get_yes_no_input() # Call the function to manage the prompt
print("Program continues after the yes/no prompt.")

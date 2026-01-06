'''
I have decided to add a dessert option(because who doesn't like dessert?)
    and added it into the functionof the program. 
    I also decided to add a tip input. As well as a fairwell message.
'''

# Request user inputs 
children_meal_price = float(input("What is the price of a child's meal? "))
adult_meal_price = float(input("What is the price of an adult's meal? "))
children_count = int(input("How many children are there? "))
adult_count = int(input("How many adults are there? "))
dessert_cost = float(input("How much does dessert cost? "))
dessert_count = int(input("How many desserts were ordered? "))

print("")

# Calculate the subtotal
subtotal = (children_meal_price * children_count) + (adult_meal_price * adult_count) + (dessert_cost * dessert_count)

print(f"Subtotal: ${subtotal:.2f}")
print("")

#Calculate sales tax and total
tax_rate = float(input("What is the sales tax rate? "))
sales_tax = (subtotal * tax_rate) / 100

print(f"Sales Tax: ${sales_tax:.2f}")

total = (subtotal + sales_tax) 

print(f"Total: ${total:.2f}")
print("")

#Calculate tip for creativity
tip = float(input("How much was the tip? "))
total_with_tip = total - tip

print(f"Your total with a tip is: ${total_with_tip}")
print("")

# Calculate Change
payment_amount = float(input("What is the payment amount? "))
change = payment_amount - total_with_tip

print(f"Change: ${change:.2f}")
print("")
print("Hope you enjoyed, have a wonderful day!")

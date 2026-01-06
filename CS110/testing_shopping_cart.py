"""
I decided to add displaying the prices of all the items before showing the total. 
I also added another option for a budget. Showing the user how much they have left in their 
budget when the get the list summary. 

I learned a new function!   

Shopping Cart Program!!!
Author: Owen Read
"""
# Variable declared:
shopping_cart_items = []
shopping_cart_prices = []
shopping_cart_total = 0
item_add = ""
item_price = ""
item_remove = ""
option = ""

print("Welcome to the Shopping Cart Program!")
print("")

while True:
    print("Menu options:")
    print("")
    print("1. Add a new item\n"
    "2. Display the contents of the shopping cart\n"
    "3. Remove item\n"
    "4. Compute the total\n"
    "5. Quit")
    option = input("Please choose a menu option 1-5: ")
    print("")
    
    # 1. Add new item + price
    if option == "1":
        item_add = input("What item would you like to add? ")
        shopping_cart_items.append(item_add)
        item_price = float(input(f"What is the price of '{item_add}'? "))
        shopping_cart_prices.append(item_price)
        print("")
        print(f"'{item_add}' has been added to the cart at ${item_price:.2f}")
        print("")

    # 2. Display contents of the shopping cart
    elif option == "2":
        print("The contents of the shopping cart are:")
        for i in range(len(shopping_cart_items)):
            print(f"{i + 1}. {shopping_cart_items[i]} - ${shopping_cart_prices[i]:.2f}")
        print("")

    # 3. Repeat #2 and remove item (( del = index .pop = value))
            # I had a really hard time figuring out how to use the .pop funcion 
            # to remove the item and the corresponding index item's price without asking for the exact price
            # and messing up the order of the list because multiple items could have the same price. 
            # if you have a clean way of using the .pop function please let me know. I had to look up
            # option of removing items from two lists with corresponding indexes and learned about the del function. 
    elif option == "3":
        print("The contents of the shopping cart are:")
        for i in range(len(shopping_cart_items)):
            print(f"{i + 1}. {shopping_cart_items[i]} - ${shopping_cart_prices[i]:.2f}")
        print("")

        item_remove_index = int(input("Which item would you like to remove? ")) - 1

        if 0 <= item_remove_index < len(shopping_cart_items):
            del shopping_cart_items[item_remove_index]
            del shopping_cart_prices[item_remove_index]
            print(f"Item '{item_remove_index + 1}' has been removed.")
            print("")
        else:
            print("That doesn't work. Please select the item number.")
            print("")
            
    # 4. Compute the total
    elif option == "4":

        for i in range(len(shopping_cart_prices)):
            price = shopping_cart_prices[i]
            print(f"${price}")
        shopping_cart_total = sum(shopping_cart_prices)
        print(f"The total price of the items in the shopping cart is ${shopping_cart_total:.2f}")
        print("")

    # 5. Quit
    elif option == "5": 
        print("Thank you for using the Shopping Cart Program! Have a wonderful day.")
        print("")
        break
    # Any other incorrect input
    else:
        print("Invalid. Please select a number 1-5.")
        print("")
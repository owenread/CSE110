payment = float(input("What is the payment amount? "))

while payment < 0:
    print("Sorry the payment cannot be negative.")


    payment = float(input("What is the payment amount? "))

print(f"The amount is ${payment:.2f}")
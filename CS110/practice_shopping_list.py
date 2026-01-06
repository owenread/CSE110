# shopping_list = []

# item = input("Item: ")
# shopping_list.append(item)

# my_list = [1, 23, 34, 355, 6]
# largest = 0

# smallest = 400

# for value in my_list:

#     if value < smallest:

#         smallest = value

# print(f"The smallest is {smallest}")
question_variable = 0
numbers = [1, 2, 3, 100]
best_so_far = -1

for number in numbers:
    if number > best_so_far:
        best_so_far = number

print(best_so_far)
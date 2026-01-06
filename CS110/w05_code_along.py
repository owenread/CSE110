"""
List of numbers 



Author: Owen Read 
"""
number = -1
number_list = []
current_smallest_number = 9999999999999999999999999999999^10
print("Please enter a series of numbers. When finished, enter '0")

while number != 0:
    number = int(input("Enter a number: "))
    
    if number != 0:
        number_list.append(number)



number_sum = sum(number_list)
print(f"The sum of the list is {number_sum}.")

number_average = number_sum / float(len(number_list))
print(f" Here is your average: {number_average}")

number_max = max(number_list)
print(f"Here is your max: {number_max}")

for number in number_list:
    if number > 0 and number < current_smallest_number:
        current_smallest_number = number
# number_min = min(number_list)
print(f"The smallest number closest to 0 that is positive is {current_smallest_number}")
# print(f"Your positive number closest to min is {number_min}.")
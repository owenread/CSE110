# '''
# This program will calculate the area of different shapes. 

# Author: Owen Read
# '''

# Calculate area of square
import math

square_side = float(input('What is the length of a side of the square in cm? '))
square_area = square_side * square_side

print(f'The area of the square in cm^2 is {square_area}')
print(f'The area of the square in mm^2 is {square_area / 10000}')
# Calculate area of a rectagle 
rectangle_length = float(input('What is the lenth of the rectangle in cm? '))
rectangle_width = float(input('What is the width of the rectangle in cm? '))
rectangle_area = rectangle_length * rectangle_width 

print(f'The area of the rectangle in cm^2 is {rectangle_area}')
print(f'The area of the rectangle in mm^2 is {rectangle_area / 10000}')
# Calculate area of a circlee 
circle_radius = float(input('What is the radius of the circle in cm? '))
circle_area_cm = math.pi * (circle_radius ** 2)
circle_area_mm = circle_area_cm / 10000

print(f'The area of the cirlce in cm^2 is {circle_area_cm}')
print(f'The area of the cirlce in mm^2 is {circle_area_mm}')

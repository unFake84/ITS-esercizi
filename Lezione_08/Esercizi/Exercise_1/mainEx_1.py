'''
    [3]
    Finally, write a simple driver program (test code) that creates instances of Circle and Rectangle,
    calls their area and perimeter methods, and prints the results.

    This will help verify that your class hierarchy works as intended.
'''

from circle import Circle
from rectangle import Rectangle

# [3]
print("-"*50)
circle_1: Circle = Circle(float(input("Set radius of circle: ")))

print("-"*50)
print(*"CIRCLE")
print(f"Area = {circle_1.area()}")
print(f"Perimeter = {circle_1.perimeter()}")

print("-"*50)
rectangle_1: Rectangle = Rectangle(float(input("Set height of rectangle: ")), float(input("Set width of rectangle: ")))

print("-"*50)
print(*"RECTANGLE")
print(f"Area = {rectangle_1.area()}")
print(f"Perimeter = {rectangle_1.perimeter()}")
print("-"*50)
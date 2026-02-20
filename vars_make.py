"""
author: Dareen Juma
date: 19/02/26
Variables Make
"""

#Input

radius = int(input("Input radius of a circle"))
length = int(input("Input length of a rectangle"))
width = int(input("Input width of a rectangle"))
oct_length = int(input("Input side length of an octagon"))

#Processing

#circle

circlearea = (3.14)*(radius**2)
circleperimeter = (2)*(3.14)*(radius)

#rectangle

rectanglearea = length*width
rectangleperimeter = 2*(length+width)

#octagon

octagonarea = 2*(1+2**0.5)*oct_length**2
octagonperimeter = 8*oct_length

#Output
print (f"The circle has an area of {circlearea} and a perimeter of {circleperimeter}")
print (f"The rectangle has an area of {rectanglearea} and a perimeter of {rectangleperimeter}")
print (f"The octagon has an area of {octagonarea} and a perimeter of {octagonperimeter}")
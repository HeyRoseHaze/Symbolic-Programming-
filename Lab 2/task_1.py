import math

radius = int(input('Enter the radius of the circle: '))

if radius < 0:
    print("The radius must be greater than zero.")
    radius = int(input('\nEnter the radius of the circle again: '))
area = math.pi * radius ** 2 
print(f'\nThe area of the cirle with radius {radius} is equal to: {area}')

circumference = 2 * math.pi * radius
print(f'\nThe circumference of the cirle with radiu {radius} is equal to: {circumference}')
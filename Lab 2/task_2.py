import math

a = int(input("Enter the coefficient a: "))
b = int(input("Enter the coefficient b: "))
c = int(input("Enter the coefficient c: "))

delta = b ** 2 - 4 * a * c 

if delta < 0:
    print('No solutions. Delta less than zero.')
elif delta == 0:
    print('One solution. Delta is equal to zero.')
    x = -b / 2*a
    print(x)
elif delta > 0:
    x1 = (-b - math.sqrt(delta)) / 2*a
    x2 = (-b + math.sqrt(delta)) / 2*a
    
    print('Two solutions. Delta is greater than zero.')
    print(x1)
    print(x2)
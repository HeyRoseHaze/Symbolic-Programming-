import math

number_a = int(input('Enter the number a: '))
number_b = int(input('Enter the number b: '))
print()

sum = number_a + number_b

print(f'The sum of the numbers "{number_a}" and "{number_b}" is equal to: {sum}\n')

difference = number_a - number_b

print(f'The difference of subtracting "{number_b}" from "{number_a}" is equal to: {difference}\n')

product = number_a * number_b

print(f'The product of the "{number_a}" and "{number_b}" is equal to: {product}\n')

quotient = number_b / number_a

print(f'The quotient of the "{number_b}" by the "{number_a}" is equal to: {quotient}\n')

root = math.sqrt(number_a + number_b)

print(f'The square root of the sum of "{number_a}" and "{number_b}" is equal to: {root}\n')

power_a = number_a ** number_b

print(f'"{number_a}" raised to the power of "{number_b}" is equal to: {power_a}\n')

power_b = number_b ** number_a

print(f'"{number_b}" raised to the power of "{number_a}" is equal to: {power_b}\n')
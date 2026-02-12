
# First way

number = int(input('Enter the number: '))
print()
dividers = []

for i in range(number, 1, -1):
    divider = (i - 1)
    if number % (divider) == 0:
        dividers.append(divider)

if sum(dividers) == number:
    print(f'Your number {number} is perfect.')
else:
    print(f"Number {number} isn't perfect number.")


# Second way

print()
dividers = []

# the greatest possible proper divisor of a number is its hald
# we only need to check up half of the number

for i in range((number // 2 ), 0, -1):
    divider = (i)
    if number % (divider) == 0:
        dividers.append(divider)

if sum(dividers) == number:
    print(f'Your number {number} is perfect.')
else:
    print(f"Number {number} isn't perfect number.")


# Third way

print()

dividers_sum = sum([i for i in range(1, number // 2 + 1) if number % i == 0])

is_perfect = (dividers_sum == number)

print(f"Is {number} perfect? {is_perfect}")
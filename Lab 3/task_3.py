

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
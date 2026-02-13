

number = (input('Enter a natural number: '))

print(f'Your number consists of {len(number)} numbers.')

total_sum = sum(int(digit) for digit in number)

print(f"The sum of the digits is: {total_sum}")

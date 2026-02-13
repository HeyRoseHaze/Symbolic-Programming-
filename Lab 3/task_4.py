

number = str(input('Enter a natural number: '))

lenght = len(number)
print(f'Your number consists of {lenght} numbers')

numbers = list(number)
sum_of_numbers = []
for i in numbers:
    num = int(i)
    sum_of_numbers.append(num)

print(f"The sum of the numbers of your numbers is equal to: {sum(sum_of_numbers)}")
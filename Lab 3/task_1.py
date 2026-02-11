

limit = int(input('Enter limit: '))
numbers = []
number = 0
while len(numbers) != limit:
    numbers.append(number)
    number += 1    

numbers_reverse = numbers.copy()
numbers_reverse.reverse()

for a, b in zip(numbers, numbers_reverse):
    print(f'{a} {b}')

# using range

limit = int(input('Enter limit: '))

for i in range(limit):
    print(i,   (limit-1) - i)
    #print(f"{i} {limit -1}")


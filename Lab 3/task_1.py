

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

# kolumna1 = [1, 2, 3, 4]
# kolumna2 = [5, 6, 7, 8]

# for a, b in zip(kolumna1, kolumna2):

#     print(f"{a:<5} {b:<5}")

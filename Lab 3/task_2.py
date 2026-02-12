import math

n = int(input('Enter the number n: '))
x = int(input('Enter the number x: '))
N = 0
e_list = []
while N != n:
    e = (x ** N) / math.factorial(N)
    e_list.append(e)
    N += 1

print(sum(e_list))
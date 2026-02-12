import math

n = int(input('Enter the number n: '))
x = float(input('Enter the number x: '))
print()

e_list = []

for i in range(n):
    e = (x ** i) / math.factorial(i)
    e_list.append(e)

series_sum = sum(e_list)

print(f"Sum of the series: {series_sum}")
print(f"Math.exp({x}): {math.exp(x)}")


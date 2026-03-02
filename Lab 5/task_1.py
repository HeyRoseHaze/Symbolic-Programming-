
def fibonacci_iterative(n):
    n1, n2 = 1, 1

    for i in range(3, n+1):
        n1, n2 = n2, n1 + n2
    return n2

for i in range(1, 51):
    print(i, fibonacci_iterative(i))
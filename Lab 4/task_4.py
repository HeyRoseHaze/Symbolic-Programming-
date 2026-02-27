def factorial_iterative(n):
    if n < 0: return None

    solution = 1

    for i in range(1, n + 1):
        solution *= i
    return solution

def factorial_recursevely(n):
    if n < 0: return None

    elif n == 0 or n == 1: return 1
    
    else:
        return n * factorial_recursevely(n-1)
    


print(factorial_iterative(3))
print(factorial_recursevely(3))
 



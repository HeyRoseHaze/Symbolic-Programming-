import timeit
import matplotlib.pyplot as plt

def fibonacci_iterative(n):
    n1, n2 = 1, 1

    for i in range(3, n+1):
        n1, n2 = n2, n1 + n2
    return n2


def fibonacci_recursively(n):
    if n < 3: return 1

    else: 
        return fibonacci_recursively(n - 1 ) + fibonacci_recursively(n - 2)
    

#start_time = timeit.default_timer()
n_i = []
time_i = []

for i in range(1, 31):
    start_time = timeit.default_timer()
    fibonacci_iterative(i)
    end_time = timeit.default_timer()
    time_iterative = end_time - start_time

    n_i.append(i)
    time_i.append(time_iterative)

n_r = []
time_r = []


for i in range(1, 31):
    start_time = timeit.default_timer()
    fibonacci_recursively(i)
    end_time = timeit.default_timer()
    time_recursively = end_time - start_time

    n_r.append(i)
    time_r.append(time_recursively)






plt.plot(n_i, time_i, label = 'iterative')
plt.plot(n_r, time_r, label = 'recursively')
plt.xlabel("n")
plt.ylabel('time')
plt.legend()
plt.show()
import math

def maclaurin_exp(x, N = 50):

    series_sum = 0
    term = 1

    for i in range(N):
        series_sum += term
        term *= x / (i + 1)

    return series_sum



# Testing the function 

x_test = 1

result = maclaurin_exp(x_test)

print(f"\nMaclaurin Sum: {result}")
print(f"Math.exp: {math.exp(x_test)}")

test_values = [1, 2, 3, -1, 5]

for i in test_values:
    result = maclaurin_exp(i)
    print(f"\nMaclaurin Sum: {result}")
    print(f"Math.exp: {math.exp(i)}")



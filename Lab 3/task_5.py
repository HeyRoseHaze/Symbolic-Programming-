import random

random_numbers = [random.randint(0, 100) for i in range(5)]

for index, value in enumerate(random_numbers):
    print(f"random_numbers[{index}] : {value}")

print(f"\nThe list consist of {len(random_numbers)} items.\n")

max_value = max(random_numbers)
max_index = random_numbers.index(max_value)

min_value = min(random_numbers)
min_index = random_numbers.index(min_value)

print(f"The largest number: {max_value} \nIndex of largest number: {max_index}\n\n"
      f"The smallest number: {min_value} \nIndex of smallest number: {min_index}")
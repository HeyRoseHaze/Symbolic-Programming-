import random

random_numbers = [random.randint(0, 100) for i in range(5)]

for index, value in enumerate(random_numbers):
    print(f"random_numbers[{index}] : {value}")

print(f"\nThe list consist of {len(random_numbers)} items.")

print(f"The largest number: {max(random_numbers)}\n"
      f"The smallest number: {min(random_numbers)}")
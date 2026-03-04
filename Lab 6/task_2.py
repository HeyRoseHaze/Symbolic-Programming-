import random

my_set1 = {random.randint(0, 10) for _ in range(10)}
my_set2 = {random.randint(0, 10) for _ in range(10)}

print(f"Set 1: {my_set1}")
print(f"Set 2: {my_set2}")

union_set = my_set1 | my_set2

intersection_set = my_set1 & my_set2

difference_set = my_set1 - my_set2

symmetric_diff_set = my_set1 ^ my_set2

print(f"Union (A ∪ B): {union_set}")
print(f"Intersection (A ∩ B): {intersection_set}")
print(f"Difference (A - B): {difference_set}")
print(f"Elements in only one set (A Δ B): {symmetric_diff_set}")
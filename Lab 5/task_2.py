import random 


def max_value(list):
    max_value = max(list)
    max_index = list.index(max_value)
    return max_value, max_index,

def min_value(list):
    min_value = min(list)
    min_index = list.index(min_value)
    return min_value, min_index

list = [random.randint(1, 100) for _ in range(10)]
print(list)
print(f'The max value and index: {max_value(list)}')
print(f'The min value and index: {min_value(list)}')
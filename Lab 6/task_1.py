
def counnter(sequence):
    counts = {}

    for item in sequence:
        if item not in counts:
            counts[item] = 1
        else:
            counts[item] += 1
    return counts

sequence = 'madagaskar'

occurance = counnter(sequence)

sorted_keys = sorted(occurance.keys())

print("Occurance count (sorted): ")
for key in sorted_keys:
    print(f'Element {key}: occurred {occurance[key]} times')

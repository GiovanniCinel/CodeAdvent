ranges = []
fresh_ingredients = 0
with open("input.txt", "r") as file:
    line = file.readline()
    while line != "\n":
        start, end = line.strip('\n').split('-')
        ranges.append([int(start), int(end)])
        line = file.readline()
    
sorted_ranges = sorted(ranges, key = lambda x : x[0])

tmp_max = 0
for range_ in sorted_ranges:
    if range_[1] > tmp_max:
        fresh_ingredients += range_[1] + 1 - max(range_[0], tmp_max + 1)
        tmp_max = range_[1]


print("The solution is:", fresh_ingredients)
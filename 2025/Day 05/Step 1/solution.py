ranges = []
ingredients = []
fresh_ingredients = 0
with open("input.txt", "r") as file:
    line = file.readline()
    while line != "\n":
        start, end = line.strip('\n').split('-')
        ranges.append([int(start), int(end)])
        line = file.readline()
    
    line = file.readline()

    while line != "":
        ingredients.append(int(line.strip('\n')))
        line = file.readline()

def isFresh(val : int):
    for range_ in ranges:
        if val in range(range_[0], range_[1] + 1):
            return True

    return False

for ingredient in ingredients:
    if isFresh(ingredient):
        fresh_ingredients += 1


print("The solution is:", fresh_ingredients)
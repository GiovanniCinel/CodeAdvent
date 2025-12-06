values = []
operations = []
total = 0

with open("input.txt", "r") as file:
    line = file.readline()
    while line[0] not in ['+', '*']:
        values.append([int(x) for x in line.strip('\n').strip().split()])
        line = file.readline()
    
    for op in line.strip('\n').split():
        operations.append(op)

for col in range(len(values[0])):
    if operations[col] == '+':
        total_column = 0
    else:
        total_column = 1
    for row in range(len(values)):
        if operations[col] == '+':
            total_column += values[row][col]
        else:
            total_column *= values[row][col]

    total += total_column

print("The solution is:", total)
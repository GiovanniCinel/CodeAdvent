values = []
operations = []
total = 0

with open("input.txt", "r") as file:
    line = file.readline()
    while line[0] not in ['+', '*']:
        values.append(line.strip("\n"))
        line = file.readline()
    
    for op in line.strip('\n').split():
        operations.append(op)

operands = []
for i in range(len(values[0]) - 1, -1, -1):
    operand = ""
    for row in range(len(values)):
        operand += values[row][i]
    if i == 0:
        operands.append(int(operand))
    if operand.strip() != "" and i > 0:
        operands.append(int(operand))
    else:
        operation = operations.pop()
        if(operation == '+'):
            tmp_total = 0
            for op in operands:
                tmp_total += op
        else:
            tmp_total = 1
            for op in operands:
                tmp_total *= op
        
        total += tmp_total
        operands.clear()

print("The solution is:", total)
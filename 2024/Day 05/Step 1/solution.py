import re

input = open("input.txt", "r")
line = input.readline()

rules = []
updates = []
total = 0

while(line != '\n'):
    endFirst = 0
    while(line[endFirst].isdigit()):
        endFirst += 1
    
    endSecond = endFirst + 1
    while(line[endSecond].isdigit()):
        endSecond += 1

    X = int(line[0 : endFirst])
    Y = int(line[endFirst + 1 : endSecond])
    
    rules.append([X, Y])
    line = input.readline()

#for i in range(0, len(rules)):
#    print(rules[i])

line = input.readline()

while(line != ""):
    updates.append(list(map(int, re.findall(r'\d+', line))))
    line = input.readline()

#for i in range(0, len(updates)):
#    print(updates)

for i in range(0, len(updates)):
    updateValid = True

    for j in range(0, len(updates[i]) - 1):
        for k in range(j+1, len(updates[i])):
            if [updates[i][k], updates[i][j]]  in rules:
                updateValid = False
    
    for j in range(len(updates[i]) - 1, 0, -1):
        for k in range(j - 1, -1, -1):
            if [updates[i][j], updates[i][k]]  in rules:
                updateValid = False

    if(updateValid):
        total += updates[i][int(len(updates[i])/2)]

print("The sum is : ", total)

input.close()
def move(map, actualPosition, step):
    UNITARYMOVEMENT = 1
    movements = [[-1,0], [0,1], [1,0], [0,-1]]
    newPosition = [actualPosition[0] + step[0], actualPosition[1] + step[1]]
    
    if map[newPosition[0]][newPosition[1]] == '.':
        map[newPosition[0]][newPosition[1]] = map[actualPosition[0]][actualPosition[1]]
        map[actualPosition[0]][actualPosition[1]] = '.'
        return newPosition
    
    if map[newPosition[0]][newPosition[1]] == '[' or map[newPosition[0]][newPosition[1]] == ']':
        otherObstaclePart = []
        if movements.index(step) % 2:
            otherObstaclePart.append(newPosition[0] + step[0])
            otherObstaclePart.append(newPosition[1] + step[1])
            move(map, otherObstaclePart, step)
            map[otherObstaclePart[0]][otherObstaclePart[1]] = map[newPosition[0]][newPosition[1]]
            map[newPosition[0]][newPosition[1]] = map[actualPosition[0]][actualPosition[1]]
            map[actualPosition[0]][actualPosition[1]] = '.'
            return newPosition
        else:
            if map[newPosition[0]][newPosition[1]] == '[':
                otherObstaclePart.append(newPosition[0] )
                otherObstaclePart.append(newPosition[1] + UNITARYMOVEMENT)
            else:
                otherObstaclePart.append(newPosition[0])
                otherObstaclePart.append(newPosition[1] - UNITARYMOVEMENT)

            move(map, newPosition, step)
            move(map, otherObstaclePart, step)

            map[newPosition[0]][newPosition[1]] = map[actualPosition[0]][actualPosition[1]]
            map[actualPosition[0]][actualPosition[1]] = '.'
            return newPosition
    return actualPosition

def isValidMove(map, actualPosition, step):
    UNITARYMOVEMENT = 1
    movements = [[-1,0], [0,1], [1,0], [0,-1]]
    newPosition = [actualPosition[0] + step[0], actualPosition[1] + step[1]]
    
    if map[newPosition[0]][newPosition[1]] == '#':
        return False
    
    if map[newPosition[0]][newPosition[1]] == '.':
        return True
    
    if map[newPosition[0]][newPosition[1]] == '[' or map[newPosition[0]][newPosition[1]] == ']':
        otherObstaclePart = []
        if movements.index(step) % 2:
            otherObstaclePart.append(newPosition[0] + step[0])
            otherObstaclePart.append(newPosition[1] + step[1])
            if isValidMove(map, otherObstaclePart, step):
                return True
        else:
            if map[newPosition[0]][newPosition[1]] == '[':
                otherObstaclePart.append(newPosition[0] )
                otherObstaclePart.append(newPosition[1] + UNITARYMOVEMENT)
            else:
                otherObstaclePart.append(newPosition[0])
                otherObstaclePart.append(newPosition[1] - UNITARYMOVEMENT)

            if isValidMove(map, newPosition, step) and isValidMove(map, otherObstaclePart, step):
                return True
    return False
    

def evaluateGPSCoordinate(map):
    FACTOR = 100
    total = 0
    for i in range(0, len(map)):
        for j in range(0, len(map[i])):
            if map[i][j] == '[':
                total += j + i * FACTOR

    return total

input = open("input.txt", "r")
line = input.readline()

map = []
newMap = []
instruction = []
robotPosition = []

possibleInstruction = ['^', '>', 'v', '<']
movements = [[-1,0], [0,1], [1,0], [0,-1]]

while(line != '\n'):
    map.append([x for x in line if x != '\n'])
    line = input.readline()

while(line != ""):
    instruction += [x for x in line if x != '\n']
    line = input.readline()

input.close()

for i in range(0, len(map)):
    temp = []
    for j in range(0, len(map[i])):
        if map[i][j] == '#' or map[i][j] == '.' :
            temp.append(map[i][j])
            temp.append(map[i][j])
        if map[i][j] == '@':
            temp.append(map[i][j])
            temp.append('.')
        if map[i][j] == 'O':
            temp.append('[')
            temp.append(']')
    newMap.append(temp)

for i in range(0, len(newMap)):
    for j in range(0, len(newMap[i])):
        if newMap[i][j] == '@':
            robotPosition.append(i)
            robotPosition.append(j)
            break

for inst in instruction:
    step = movements[possibleInstruction.index(inst)]
    if isValidMove(newMap, robotPosition, step):
        robotPosition = move(newMap, robotPosition, step)

total = evaluateGPSCoordinate(newMap)

print("The total is : ", total)
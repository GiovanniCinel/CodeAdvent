def move(map, actualPosition, step):
    newPosition = [actualPosition[0] + step[0], actualPosition[1] + step[1]]
    if map[newPosition[0]][newPosition[1]] == '#':
        return False, actualPosition
    
    if map[newPosition[0]][newPosition[1]] == '.':
        map[newPosition[0]][newPosition[1]] = map[actualPosition[0]][actualPosition[1]]
        map[actualPosition[0]][actualPosition[1]] = '.'
        return True, newPosition
    
    if map[newPosition[0]][newPosition[1]] == 'O' and move(map, newPosition, step)[0]:
        map[newPosition[0]][newPosition[1]] = map[actualPosition[0]][actualPosition[1]]
        map[actualPosition[0]][actualPosition[1]] = '.'
        return True, newPosition
    
    return False, actualPosition
    

def evaluateGPSCoordinate(map):
    FACTOR = 100
    total = 0
    for i in range(0, len(map)):
        for j in range(0, len(map[i])):
            if map[i][j] == 'O':
                total += j + i * FACTOR

    return total

input = open("input.txt", "r")
line = input.readline()

map = []
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
    for j in range(0, len(map[i])):
        if map[i][j] == '@':
            robotPosition.append(i)
            robotPosition.append(j)
            break

for inst in instruction:
    step = movements[possibleInstruction.index(inst)]
    done, robotPosition = move(map, robotPosition, step)

total = evaluateGPSCoordinate(map)

print("The total is : ", total)
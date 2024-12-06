import numpy as np
import copy

def printMap(map):
    for i in range(0, len(map)):
        line_i = ""
        for j in range(0, len(map[i])):
            line_i += map[i][j]
        print(line_i)

def mapHasLoop(map, actualPosition, actualDirection, offsets):
    tracer = ['|','-','|','-']
    allMovement = '+'
    allDirectionClosed = 0
    hit = []
    while(actualPosition[0] in range(0, len(map)) and actualPosition[1] in range(0, len(map[actualPosition[0]]))):
        nextPosition = actualPosition + offsets[actualDirection]
        if(nextPosition[0] not in range(0, len(map)) or nextPosition[1] not in range(0, len(map[nextPosition[0]]))):
            return False

        if(map[nextPosition[0]][nextPosition[1]] == '#' or map[nextPosition[0]][nextPosition[1]] == '0'):
            if([[nextPosition[0], nextPosition[1]], actualDirection] in hit):
                return True
            hit.append([[nextPosition[0], nextPosition[1]], actualDirection])
            map[actualPosition[0]][actualPosition[1]] = allMovement
            actualDirection += 1
            actualDirection = actualDirection % 4
            allDirectionClosed +=1

            if(allDirectionClosed == 4):
                return True
        else:
            if(map[actualPosition[0]][actualPosition[1]] == tracer[(actualDirection+1) % 4]):
                map[actualPosition[0]][actualPosition[1]] = allMovement
            else:
                map[actualPosition[0]][actualPosition[1]] = tracer[actualDirection]
            actualPosition = nextPosition
            allDirectionClosed = 0
    return False



input = open("input.txt", "r")
map = []
directions = ['^','>','v','<']
offsets = np.array([[-1,0],[0,1],[1,0],[0,-1]])
actualDirection = -1
actualPosition = np.array([-1, -1])
total = 0

line = input.readline()

while(line != ""):
    vec = []
    for c in line:
        if c != '\n':
            vec.append(c)
    map.append(vec)
    line = input.readline()

input.close()

for i in range(0, len(map)):
        for j in range(0, len(map[i])):
            if map[i][j] in directions:
                actualDirection = directions.index(map[i][j])
                actualPosition = [i, j]

for i in range(0, len(map)):
    for j in range(0, len(map[i])):
        step += 1
        if(actualPosition != [i, j] and map[i][j] != '#'):
            tempMap = copy.deepcopy(map)
            tempMap[i][j] = '0'
            if mapHasLoop(tempMap, copy.deepcopy(actualPosition), actualDirection, offsets):
                total += 1


print("In ", total, " position we can add an obstacol to stuck the guard in a loop.")
import numpy as np

def printMap(map):
    for i in range(0, len(map)):
        line_i = ""
        for j in range(0, len(map[i])):
            line_i += map[i][j]
        print(line_i)

def countXPosition(map):
     total = 0
     for i in range(0, len(map)):
        for j in range(0, len(map[i])):
            if map[i][j] == 'X':
                total += 1
     return total


input = open("input.txt", "r")
map = []
directions = ['^','>','v','<']
offsets = np.array([[-1,0],[0,1],[1,0],[0,-1]])
actualDirection = -1
actualPosition = np.array([-1, -1])

line = input.readline()

while(line != ""):
    vec = []
    for c in line:
        vec.append(c)
    map.append(vec)
    line = input.readline()

input.close()

for i in range(0, len(map)):
        for j in range(0, len(map[i])):
            if map[i][j] in directions:
                actualDirection = directions.index(map[i][j])
                actualPosition = [i, j]

while(actualPosition[0] in range(0, len(map)) and actualPosition[1] in range(0, len(map[actualPosition[0]]))):
    map[actualPosition[0]][actualPosition[1]] = 'X'
    nextPosition = actualPosition + offsets[actualDirection]
    if(map[nextPosition[0]][nextPosition[1]] == '#'):
        actualDirection += 1
        actualDirection = actualDirection % 4
    else:
        actualPosition = nextPosition
        


print("The guard visit ", countXPosition(map), " distinct position before left the area.")
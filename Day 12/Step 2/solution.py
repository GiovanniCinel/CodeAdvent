def calculatePerimeter(perimeter):
    perimeterForOrientation = []
    perimeterValue = 0
    for step in INCREMENTS:
        perimeterForOrientation.append([x for x in perimeter if x[2] == step])
    for orientation in perimeterForOrientation:
        coord = []
        sameCoord = []
        if abs(orientation[0][2][0]) == 1: 
            index = 0
            oppositeIndex = 1
        else:
            index = 1
            oppositeIndex = 0

        for i in orientation:
            if i[index] not in coord:
                coord.append(i[index])

        for i in coord:
            sameCoord.append([j for j in orientation if j[index] == i])

        for i in sameCoord:
            i.sort(key=lambda x: x[oppositeIndex])
            perimeterValuePartial = 1
            for j in range(1, len(i)):
                if(i[j-1][oppositeIndex]+1 != (i[j][oppositeIndex])):
                    perimeterValuePartial +=1

            perimeterValue +=perimeterValuePartial
    return perimeterValue

def expandArea(row, column, map, checkMap):
    checkMap[row][column] = False
    perimeter = []
    area = 1
    for step in INCREMENTS:
        newRow = row + step[0]
        newCol = column + step[1]
        if(newRow in range(0, len(map)) and newCol in range(0, len(map[newRow])) and checkMap[newRow][newCol] and map[row][column] == map[newRow][newCol]):
            additionalPerimeter, additionalArea = expandArea(newRow, newCol, map, checkMap)
            area += additionalArea
            perimeter += additionalPerimeter
        else:
            if(newRow in range(0, len(map)) and newCol in range(0, len(map[newRow]))):
                if(map[row][column] != map[newRow][newCol]):
                    perimeter.append([row,column, step])
            else:
                perimeter.append([row,column, step])  

    return perimeter, area

input = open("input.txt", "r")
line = input.readline()

INCREMENTS = [[1,0],[0,1],[-1,0],[0,-1]]

map = []
checkMap = []
total = 0

while(line != ""):
    map.append([x for x in line if x != '\n'])
    checkMap.append([True for x in line if x != '\n'])
    line = input.readline()

input.close()

for i in range(0, len(map)):
    for j in range(0, len(map[i])):
        if checkMap[i][j]:
            perimeter, area =  expandArea(i, j, map, checkMap)
            perimeterValue = calculatePerimeter(perimeter)
            total += perimeterValue * area

print("The total price is : ", total)
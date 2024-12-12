def expandArea(row, column, map, checkMap):
    increments = [[1,0],[0,1],[-1,0],[0,-1]]
    checkMap[row][column] = False
    perimeter = 0
    area = 1
    for step in increments:
        newRow = row + step[0]
        newCol = column + step[1]
        if(newRow in range(0, len(map)) and newCol in range(0, len(map[newRow])) and checkMap[newRow][newCol] and map[row][column] == map[newRow][newCol]):
            additionalPerimeter, additionalArea = expandArea(newRow, newCol, map, checkMap)
            area += additionalArea
            perimeter += additionalPerimeter
        else:
            if(newRow in range(0, len(map)) and newCol in range(0, len(map[newRow]))):
                if(map[row][column] != map[newRow][newCol]):
                    perimeter += 1
            else:
                perimeter += 1  

    return perimeter, area

input = open("input.txt", "r")
line = input.readline()

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
            total += perimeter * area

print("The total price is : ", total)
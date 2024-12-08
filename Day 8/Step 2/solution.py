def printMap(map):
    for i in range(0, len(map)):
        str = ""
        for j in range(0, len(map[i])):
            str += map[i][j]
        print(str)

from collections import defaultdict

input = open("input.txt", "r")
line = input.readline()

map = defaultdict(list)
antinodeMap = []
total = 0

row = 0
while(line != ""):
    column = 0
    antinodeMap.append([x for x in line if x != '\n'])
    for char in line:
        if(char not in map.keys()):
            map[char] = [[row, column]]
        else:
            map[char].append([row, column])
        column += 1
    line = input.readline()
    row += 1

input.close()

map.pop('.')
map.pop('\n')

for key in map.keys():
    for i in range(0, len(map[key])):
        for j in range(0, len(map[key])):
            if(j != i):
                rowI = map[key][i][0]
                colI = map[key][i][1]
                rowJ = map[key][j][0]
                colJ = map[key][j][1]
                deltaRow = rowJ - rowI
                deltaCol = colJ - colI
                antennaRow = rowJ
                antennaCol = colJ
                while((antennaRow in range(0, len(antinodeMap))) and (antennaCol in range(0, len(antinodeMap[antennaRow])))):
                    antinodeMap[antennaRow][antennaCol] = '#'
                    antennaRow = antennaRow + deltaRow
                    antennaCol = antennaCol + deltaCol

#printMap(antinodeMap)

for i in range(0, len(antinodeMap)):
        for j in range(0, len(antinodeMap[i])):
            if(antinodeMap[i][j] == '#'):
                total += 1

print("The number of distinct antinodes is : ", total)
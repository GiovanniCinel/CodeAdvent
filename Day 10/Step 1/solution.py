def score(map, position):
    if(map[position[0]][position[1]] == 9):
        return [[position[0], position[1]]]
    
    movement = [[1,0],[0,1],[-1,0],[0,-1]]
    peakPositions = []
    for step in movement:
        newPosition = [position[0] + step[0], position[1] + step[1]]
        if(newPosition[0] not in range(0, len(map)) or newPosition[1] not in range(0, len(map[newPosition[0]]))):
            continue
        if(map[position[0]][position[1]] + 1 == map[newPosition[0]][newPosition[1]]):
            partialPeakPositions = score(map, newPosition)
            for peak in partialPeakPositions:
                peakPositions.append(peak)
    return peakPositions


def trailheadsSearch(map):
    trailheads = []
    for row in range(0, len(map)):
        for col in range(0, len(map[row])):
            if map[row][col] == 0:
                trailheads.append([row, col])
    return trailheads


input = open("input.txt", "r")
line = input.readline()

map = []
total = 0

while(line != ""):
    map.append([int(ch) for ch in line if ch != '\n' ])
    line = input.readline()

input.close()

trailheads = trailheadsSearch(map)

for trailhead in trailheads:
    peakPositions = score(map, trailhead)
    for i in range(0, len(peakPositions)):
        if(peakPositions[i] not in peakPositions[0:i]):
            total = total + 1

print("The total score of the trailhead is : ", total)
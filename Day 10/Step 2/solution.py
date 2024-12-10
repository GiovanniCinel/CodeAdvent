def score(map, position):
    if(map[position[0]][position[1]] == 9):
        return 1
    
    movement = [[1,0],[0,1],[-1,0],[0,-1]]
    partialScore = 0
    for step in movement:
        newPosition = [position[0] + step[0], position[1] + step[1]]
        if(newPosition[0] not in range(0, len(map)) or newPosition[1] not in range(0, len(map[newPosition[0]]))):
            continue
        if(map[position[0]][position[1]] + 1 == map[newPosition[0]][newPosition[1]]):
            partialScore += score(map, newPosition)
    return partialScore


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
    total += score(map, trailhead)

print("The total score of the trailhead is : ", total)
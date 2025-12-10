red_tiles = []
max_square = 0

with open("input.txt", "r") as file:
    line = file.readline()
    while line != "":
        red_tiles.append([int(coord) for coord in line.strip('\n').split(",")])
        line = file.readline()

for first_corner_index in range(len(red_tiles)):
    for second_corner_index in range(first_corner_index + 1, len(red_tiles)):
        square = (max(red_tiles[first_corner_index][0], red_tiles[second_corner_index][0]) + 1 - min(red_tiles[first_corner_index][0], red_tiles[second_corner_index][0])) * (max(red_tiles[first_corner_index][1], red_tiles[second_corner_index][1]) + 1 - min(red_tiles[first_corner_index][1], red_tiles[second_corner_index][1]))
        if square > max_square:
            max_square = square

print("The solution is:", max_square)
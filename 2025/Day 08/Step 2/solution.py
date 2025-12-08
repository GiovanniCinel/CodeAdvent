import math
boxes = []
map_boxes = []

with open("input.txt", "r") as file:
    line = file.readline()
    while line != "":
        boxes.append([int(coord) for coord in line.strip('\n').split(',')])
        line = file.readline()

def distance(coord_1, coord_2):
    return math.sqrt((coord_1[0] - coord_2[0])**2 + (coord_1[1] - coord_2[1])**2 + (coord_1[2] - coord_2[2])**2)

for index_1 in range(len(boxes)):
    for index_2 in range(index_1 + 1, len(boxes)):
        key = distance(boxes[index_1], boxes[index_2])
        map_boxes.append([key, boxes[index_1], boxes[index_2]])

map_boxes.sort(key = lambda elem:  elem[0])

circuits = []
finish = False
for counter in range(len(map_boxes)):
    if finish:
        break
    done = False
    boxes = map_boxes[counter]
    if not len(circuits):
        circuits.append([boxes[1], boxes[2]])
        continue
    for circuit_1 in range(len(circuits)):
        if boxes[1] in circuits[circuit_1]:
            if boxes[2] in circuits[circuit_1]:
                done = True
                break
            for circuit_2 in range(len(circuits)):
                if boxes[2] in circuits[circuit_2]:
                    circuits[circuit_1].extend(circuits[circuit_2])
                    del circuits[circuit_2]
                    if len(circuits[0]) == 1000:
                        print("The solution is:", boxes[1][0] * boxes[2][0])
                        finish = True
                    done = True
                    break
            if done:
                break
            circuits[circuit_1].extend([boxes[2]])
            if len(circuits[0]) == 1000:
                print("The solution is:", boxes[1][0] * boxes[2][0])
                finish = True
            done = True
            break
    if done:
        continue

    for circuit_1 in range(len(circuits)):
        if boxes[2] in circuits[circuit_1]:
            circuits[circuit_1].extend([boxes[1]])
            if len(circuits[0]) == 1000:
                print("The solution is:", boxes[1][0] * boxes[2][0])
                finish = True
            done = True
            break
    if done:
        continue

    circuits.append([boxes[1], boxes[2]])
    if len(circuits[0]) == 1000:
        print("The solution is:", boxes[1][0] * boxes[2][0])
        finish = True
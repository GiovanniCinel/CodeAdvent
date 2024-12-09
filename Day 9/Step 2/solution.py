input = open("input.txt", "r")
line = input.readline()
diskMap = [int(x) for x in line if x != '\n']
input.close()

diskMapRepresentation = []
indices = []
total = 0

for i in range(0, len(diskMap)):
    if(i % 2):
        for j in range(0, diskMap[i]):
            diskMapRepresentation.append('.')
    else:
        indices.append(len(diskMapRepresentation))
        for j in range(0, diskMap[i]):
            diskMapRepresentation.append(int(i/2))


i = len(diskMapRepresentation)
for k in range(len(indices)-1, -1, -1):
    size = i - indices[k]
    start = 0 
    j = 0
    actualSize = 0
    while(actualSize < size):
        if(j > indices[k]):
            break
        if(diskMapRepresentation[j] == '.'):
            actualSize += 1
            j += 1
        else:
            actualSize = 0
            j += 1
            start = j

    if(j > indices[k]):
        i = indices[k] - 1

        while(diskMapRepresentation[i] == '.'):
            i -= 1
        i += 1
        continue

    for shift in range(0, size):
        diskMapRepresentation[start + shift] = diskMapRepresentation[indices[k] + shift]
        diskMapRepresentation[indices[k] + shift] = '.'


    i = indices[k] - 1

    while(diskMapRepresentation[i] == '.'):
        i -= 1
    i += 1


for l in range(0, len(diskMapRepresentation)):
    if diskMapRepresentation[l] != '.':
        total += diskMapRepresentation[l] * l

print("The resulting filesystem checksum is : ", total)
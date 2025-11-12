input = open("input.txt", "r")
line = input.readline()
diskMap = [int(x) for x in line if x != '\n']
input.close()

diskMapRepresentation = []
total = 0

for i in range(0, len(diskMap)):
    if(i % 2):
        for j in range(0, diskMap[i]):
            diskMapRepresentation.append('.')
    else:
        for j in range(0, diskMap[i]):
            diskMapRepresentation.append(int(i/2))

j = 0
for i in range(len(diskMapRepresentation)-1, 0, -1):
    if(j > i ):
        break
    if(diskMapRepresentation[i] != '.'):
        while(diskMapRepresentation[j] != '.'):
            j += 1
        if(j < i):
            diskMapRepresentation[j] = diskMapRepresentation[i]
            diskMapRepresentation[i] = '.'

i = 0
while (diskMapRepresentation[i] != '.'):
    total += diskMapRepresentation[i] * i
    i += 1

print("The resulting filesystem checksum is : ", total)
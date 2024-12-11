import re 
import copy

BLINKING_TIMES = 25
FACTOR = 2024

input = open("input.txt", "r")
line = input.readline()
input.close()

stones = [int(num) for num in re.findall(r'-?\d+', line)]

for i in range(0, BLINKING_TIMES):
    print(i)
    temp = []
    for j in stones:
        if(j == 0):
            temp.append(1)
        else:
            length = len(str(j))
            if(length % 2):
                temp.append(j * FACTOR)
            else:
                length = int(length/2)
                first = int(str(j)[0:length])
                second = int(str(j)[length:])
                temp.append(first)
                while(str(second)[0] == "0" and len(str(second)) > 1):
                    second = int(str(second)[1:])
                temp.append(second)
                
    stones = copy.deepcopy(temp)

print("Now we have ", len(stones), " stones")
def findOperation(result, vec, partial):
    if partial > result:
        False
    if(len(vec) == 1):
        if(result == partial * vec[0]):
            return True
        if(result == partial + vec[0]):
            return True
        return False
    
    mulWay = partial * vec[0]
    sumWay = partial + vec[0]

    if(findOperation(result, vec[1:], mulWay) or findOperation(result, vec[1:], sumWay)):
        return True
    return False


import re
input = open("input.txt", "r")

line = input.readline()
data = []
total = 0

while(line != ""):
    data.append(list(map(int, re.findall(r'\d+', line))))
    line = input.readline()

input.close()

for i in range(0, len(data)):
    result = data[i][0]
    if(findOperation(result, data[i][2:], data[i][1])):
        total += result

print("The total sum is: ", total)
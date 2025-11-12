import numpy as np

input = open("input.txt", "r")
line = input.readline()

vec1 = []
vec2 = []

i = 1

while(line != ""):
    num1, num2 = map(int, line.split())
    i+=1
    vec1.append(num1)
    vec2.append(num2)
    line = input.readline()

vec1.sort()
vec2.sort()

npvec1 = np.array(vec1)
npvec2 = np.array(vec2)

result = abs(npvec1 - npvec2)

input.close()

print(result.sum())
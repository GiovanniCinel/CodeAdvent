import numpy as np

input = open("input.txt", "r")

line = input.readline()
similarityFactor = 0
vec1 = []
vec2 = []

while(line != ""):
    num1, num2 = map(int, line.split())
    
    vec1.append(num1)
    vec2.append(num2)
    
    line = input.readline()

for elem1 in vec1:
    count = 0
    
    for elem2 in vec2:
        if(elem1 == elem2):
            count += 1

    similarityFactor += count * elem1

input.close()

print(similarityFactor)
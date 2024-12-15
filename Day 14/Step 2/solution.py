import re
import numpy as np
from itertools import count

def treeConfiguration(space):
    
    return False

WIDE = 101
TALL = 103

input = open("input.txt", "r")
line = input.readline()

time = 1
inf = float("inf")
positions = []
velocities = []

while(line != ""):
    x, y, vX, vY = map(int, re.findall(r'-?\d+', line))
    positions.append([x,y])
    velocities.append([vX,vY])
    line = input.readline()

input.close()

npPositions = np.array(positions)
npVelocities = np.array(velocities)

while(time):
    space = np.zeros((TALL, WIDE))
    for j in range(0, len(npPositions)):
        npPositions[j] += npVelocities[j]

    for i in range(0, len(npPositions)):
        while(npPositions[i][0] < 0):
            npPositions[i][0] += WIDE
        while(npPositions[i][1] < 0):
            npPositions[i][1] += TALL 
        if(npPositions[i][0] >= WIDE):
            npPositions[i][0] %= WIDE
        if(npPositions[i][1] >= TALL):
            npPositions[i][1] %= TALL
        space[npPositions[i][1]][npPositions[i][0]] += 1
    
    halfWide = int(WIDE/2)
    halfTall = int(TALL/2)

    q1, q2, q3, q4 = 0, 0, 0, 0

    for i in range(0, halfTall):
        for j in range(0, halfWide):
            q1 += space[i][j]

    for i in range(0, halfTall):
        for j in range(halfWide + 1, WIDE):
            q2 += space[i][j]

    for i in range(halfTall + 1, TALL):
        for j in range(0, halfWide):
            q3 += space[i][j]

    for i in range(halfTall + 1, TALL):
        for j in range(halfWide + 1, WIDE):
            q4 += space[i][j]
    
    sf = q1 * q2 * q3 * q4
    
    if sf < inf:
        inf = sf
        bestIteration = time

    time += 1

    if(time > 10**4):
        break

print("The safety factor is : ", bestIteration)
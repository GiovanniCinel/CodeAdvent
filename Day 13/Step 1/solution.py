import re
import sympy as sp

input = open("input.txt", "r")

line = input.readline()

a = []
b = []
prizes = []
aCost = 3
bCost = 1
total = 0

while (line != ""):
    x, y = map(int, re.findall(r'-?\d+', line))
    a.append([x,y])
    line = input.readline()
    x, y = map(int,re.findall(r'-?\d+', line))
    b.append([x,y])
    line = input.readline()
    x, y = map(int, re.findall(r'-?\d+', line))
    prizes.append([x,y])
    line = input.readline()
    line = input.readline()


for i in range(0, len(prizes)):
    aX = a[i][0]
    aY = a[i][1]

    bX = b[i][0]
    bY = b[i][1]

    prizeX = prizes[i][0]
    prizeY = prizes[i][1]

    nA, nB = sp.symbols("nA nB")

    eq1 = sp.Eq(aX * nA + bX * nB, prizeX)
    eq2 = sp.Eq(aY * nA + bY * nB, prizeY)
    
    
    dictSolutions = sp.solve((eq1, eq2), (nA, nB))
    solutions = [dictSolutions[nA], dictSolutions[nB]]


    if(len(solutions) > 0 and solutions[0].is_integer and solutions[1].is_integer and solutions[0] < 101 and solutions[1] < 101):
        total += solutions[0] * aCost + solutions[1] * bCost

print("The minimum cost is : ", total)
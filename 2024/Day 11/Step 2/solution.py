from functools import lru_cache
import re

@lru_cache(maxsize=None)
def blinking(stone, iter):
    if iter == 0:
        return 1
    
    if(stone == 0):
        return blinking(1, iter -1)
    else:
        length = len(str(stone))
        if(length % 2):
            return blinking(stone * FACTOR, iter - 1)
        else:
            length = int(length/2)
            first = int(str(stone)[0:length])
            second = int(str(stone)[length:])
            while(str(second)[0] == "0" and len(str(second)) > 1):
                second = int(str(second)[1:])
            return blinking(first, iter - 1) + blinking(second, iter - 1)

BLINKING_TIMES = 75
FACTOR = 2024
total = 0

input = open("input.txt", "r")
line = input.readline()
input.close()

stones = [int(num) for num in re.findall(r'-?\d+', line)]

for j in stones:
    total += blinking(j, BLINKING_TIMES) 

print("Now we have ", total, " stones")

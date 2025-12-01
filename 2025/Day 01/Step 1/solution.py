LAP = 100

position = 50
zero_counter = 0

with open("input.txt ", "r") as f:
    rotations = f.readlines()

for rotation in rotations:
    direction = rotation[:1]
    step = int(rotation[1:])

    if direction == 'R':
        position = (position + step) % LAP
    else:
        position = (position - step) % LAP
    
    if position == 0:
        zero_counter += 1

print("The solution is:", zero_counter)
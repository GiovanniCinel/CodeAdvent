LAP = 100

position = 50
zero_counter = 0

with open("input.txt ", "r") as f:
    rotations = f.readlines()

for rotation in rotations:
    direction = rotation[:1]
    step = int(rotation[1:])
    while step >= LAP:
        step -= LAP
        zero_counter += 1

    if step == 0:
        continue

    if direction == 'R':
        old_position = position
        position = (position + step) % LAP
        if old_position > position and old_position != 0 and position != 0: zero_counter += 1
    else:
        old_position = position
        position = (position - step) % LAP
        if old_position < position and old_position != 0 and position != 0: zero_counter += 1

    if position == 0:
        zero_counter += 1        

print("The solution is:", zero_counter)
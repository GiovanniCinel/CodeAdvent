with open("input.txt", "r") as file:
    lines = file.readlines()

roll_removed = 0

def removeRoll():
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if lines[row][col] == '@':
                roll_adjacent = 0
                for i in range(max(0, row - 1), min(len(lines), row + 2)):
                    for j in range(max(0, col - 1), min(len(lines[row]), col + 2)):
                        if i == row and j == col:
                            continue
                        if(lines[i][j] == '@'):
                            roll_adjacent += 1
                
                if roll_adjacent < 4:
                    lines[row] = lines[row][:col] + '.' + lines[row][col+1:]
                    return True
                
    return False
while removeRoll():
    roll_removed += 1

print("The solution is:", roll_removed)
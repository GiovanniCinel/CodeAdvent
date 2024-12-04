input = open("input.txt", "r")
line = input.readline()

text = []
counter = 0

while(line != ""):
    row = []
    for i in range(0, len(line)):
        row.append(line[i])
    
    text.append(row)
    line = input.readline()

input.close()

# Orizontal search
for i in range(0, len(text)):
    for j in range(0, len(text[i]) - 3):
        if(text[i][j:j+4] == ['X', 'M', 'A', 'S'] or text[i][j:j+4] == ['S', 'A', 'M', 'X']):
            counter += 1

# Vertical search
for i in range(0, len(text[0])):
    for j in range(0, len(text) - 3):
        temp = []
        for l in range(0, 4):
            temp.append(text[j+l][i])
        if(temp == ['X', 'M', 'A', 'S'] or temp == ['S', 'A', 'M', 'X']):
            counter += 1

# Diagonal search
for i in range(0, len(text) - 3):
    for j in range(0, len(text[i]) - 3):
        temp = []
        for l in range(0, 4):
            temp.append(text[i+l][j+l])
        if(temp == ['X', 'M', 'A', 'S'] or temp == ['S', 'A', 'M', 'X']):
            counter += 1

for i in range(len(text) - 1, 2, -1):
    for j in range(0, len(text[i]) - 3):
        temp = []
        for l in range(0, 4):
            temp.append(text[i-l][j+l])
        if(temp == ['X', 'M', 'A', 'S'] or temp == ['S', 'A', 'M', 'X']):
            counter += 1

print("XMAS world found : ", counter)
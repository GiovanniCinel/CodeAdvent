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

for i in range(1, len(text) - 1):
    for j in range(1, len(text[i]) - 1):
        if(text[i][j] == 'A'):
            if((text[i - 1][j - 1] == 'M' and text[i + 1][j + 1] == 'S') or (text[i - 1][j - 1] == 'S' and text[i + 1][j + 1] == 'M')):
                if((text[i + 1][j - 1] == 'M' and text[i - 1][j + 1] == 'S') or (text[i + 1][j - 1] == 'S' and text[i - 1][j + 1] == 'M')):
                    counter += 1

print("XMAS found : ", counter)
with open("input.txt", "r") as file:
    lines = file.readlines()

total_joltage = 0
JOLTAGE_LEN = 12

for line in lines:
    max_joltage = ""
    len_line = len(line) - 1
    chosen = 0
    last_chosen = -1

    while chosen < JOLTAGE_LEN:
        max = 0
        for i in range(last_chosen + 1, len_line - (JOLTAGE_LEN - chosen - 1)):
            if int(line[i]) > max:
                max = int(line[i])
                actual_index = i
        max_joltage += str(max)
        last_chosen = actual_index
        chosen += 1    

    total_joltage += int(max_joltage)

print("The solution is:", total_joltage)
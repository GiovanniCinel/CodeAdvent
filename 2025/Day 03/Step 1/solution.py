with open("input.txt", "r") as file:
    lines = file.readlines()

total_joltage = 0

for line in lines:
    max_joltage = 0
    for decimal in range(len(line) - 1):
        if int(line[decimal]) < max_joltage // 10:
            continue
        for unit in range(decimal + 1, len(line)):
            if(max_joltage < int(line[decimal] + line[unit])):
                max_joltage = int(line[decimal] + line[unit])

    total_joltage += max_joltage


print("The solution is:", total_joltage)
input = open("input.txt", "r")
line = input.readline()

safe_report_counter = 0

while(line != ""):
    report = []
    report = [int(num) for num in line.split()]

    asc, desc = True, True
    for i in range(0, len(report)-1):
        if(report[i] >= report[i + 1]):
            asc = False
        if(report[i] <= report[i + 1]):
            desc = False
        if(abs(report[i + 1] - report[i]) > 3):    
            asc, desc = False, False
    
    if(asc or desc):
        safe_report_counter +=1

    line = input.readline()

input.close()

print("Safe report: ", safe_report_counter)
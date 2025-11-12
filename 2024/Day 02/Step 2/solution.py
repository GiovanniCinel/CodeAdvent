def step_control(vector):
    for i in range(0, len(vector)-1):
        if(abs(vector[i] - vector[i + 1]) > 3):
            return False
    return True

def is_ascent(vector):
    for i in range(0, len(vector)-1):
        if(vector[i] >= vector[i + 1]):
            return False
    return True

def is_descent(vector):
    for i in range(0, len(vector)-1):
        if(vector[i] <= vector[i + 1]):
            return False
    return True

input = open("input.txt", "r")
line = input.readline()

safe_report_counter = 0

while(line != ""):
    report = [int(num) for num in line.split()]
    
    if((is_ascent(report) or is_descent(report)) and step_control(report)):
        safe_report_counter +=1
    else:
        acceptable = False
        for i in range(0, len(report)):
            new_report = report[ : i] + report[i+1 : ]
            if((is_ascent(new_report) or is_descent(new_report)) and step_control(new_report)):
                acceptable = True
        if acceptable:
            safe_report_counter +=1

    line = input.readline()

input.close()

print("Safe report: ", safe_report_counter)
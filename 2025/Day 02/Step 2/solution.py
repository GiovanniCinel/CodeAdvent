with open("input.txt", "r") as file:
    line = file.readline()

intervals = line.strip(",").split(",")

invalid_id_sum = 0

for interval in intervals:
    start, end = interval.split("-")
    for id in range(int(start), int(end) + 1 ):
        id_added = False
        s_id = str(id)
        len_id = len(s_id)

        for div in range(2, len_id + 1):
            if id_added:
                break
            if len_id % div:
                continue
            step_distance = len_id // div
            for step in range(2 * step_distance, len_id + 1, step_distance):
                if s_id[step - 2 * step_distance:step - step_distance] != s_id[step - step_distance:step]:
                    break
                if step == len_id and not id_added:
                    id_added = True
                    invalid_id_sum += id

print("The solution is:", invalid_id_sum)
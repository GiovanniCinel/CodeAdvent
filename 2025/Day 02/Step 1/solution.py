with open("input.txt", "r") as file:
    line = file.readline()

intervals = line.strip(',').split(',')

invalid_id_sum = 0

for interval in intervals:
    start, end = interval.split('-')
    for id in range(int(start), int(end) + 1):
        s_id = str(id)
        len_id = len(s_id) 
        if len_id % 2:
            continue
        len_id //= 2

        if s_id[:len_id] == s_id[len_id:]:
            invalid_id_sum += id

print("Solution is:", invalid_id_sum)

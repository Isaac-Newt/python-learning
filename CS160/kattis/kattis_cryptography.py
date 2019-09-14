import fileinput

for line in fileinput.input():
    per_reps = len(line)/3
    target = int(per_reps) * "PER"

    day_count = 0
    for index in range(len(line.strip())):
        if line[index] != target[index]:
            day_count += 1
        
    print(day_count)

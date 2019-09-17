import fileinput

for line in fileinput.input():
    line = line.strip()
    list = line.split()
    int1 = int(list[0])
    int2 = int(list[1])

    difference = abs(int1 - int2)
    print(difference)
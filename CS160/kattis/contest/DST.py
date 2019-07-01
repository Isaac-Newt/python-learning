import fileinput
import sys

line = sys.stdin.readline()
test_count = int(line)

while test_count > 0:
    line = sys.stdin.readline()
    line = line.strip()
    list = line.split()
    direct = list[0]
    change = int(list[1])
    cur_hr = int(list[2])
    cur_mn = int(list[3])

    new_hr = 0
    new_mn = 0

    if direct == "F":
        new_mn = cur_mn + (change % 60)
        if new_mn >= 60:
            new_hr += 1
            new_mn = new_mn - 60

        new_hr = new_hr + cur_hr + (change // 60)
        if new_hr>= 24:
            new_hr = new_hr - 24

    elif direct == "B":
        new_mn = cur_mn - (change % 60)
        if new_mn < 0:
            new_hr -= 1
            new_mn = new_mn + 60

        new_hr = new_hr + cur_hr - (change // 60)
        if new_hr < 0:
            new_hr = new_hr + 24

    print(new_hr, new_mn)
    test_count -= 1

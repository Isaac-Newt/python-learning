import fileinput
import sys

def find_soda(e, c):
    return (e // c), (e % c)

for line in fileinput.input():
    line = line.strip()
    list = line.split()
    empty = (int(list[0]) + int(list[1]))
    requd = int(list[2])
    new = 0
    while empty >= requd:
        new_sodas, remainder = find_soda(empty, requd)
        empty = new_sodas + remainder
        new += new_sodas
    print(new)
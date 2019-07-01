import fileinput
import sys

def find_req_bribes(art, imp):
    return (art * (imp - 1)) + 1

for line in fileinput.input():
    line = line.strip()
    list = line.split()
    art_ct = int(list[0])
    impact = int(list[1])
    print(find_req_bribes(art_ct, impact))

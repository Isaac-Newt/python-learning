l = []
d = {}
for num in range(100000000):
    l.append(num)
    d[num] = None

print("Z in Dict: ", "z" in d)
print("Z in List: ", "z" in l)
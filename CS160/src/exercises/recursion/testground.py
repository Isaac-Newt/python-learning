spaces_count = 0
levels = 5
star_count = levels

for count in range(levels):
    stars = "*" * (2 * star_count - 1)
    spaces = " " * spaces_count
    print(spaces + stars + spaces)
    star_count -= 1
    spaces_count += 1

star_count = 3
spaces_count = ((2 * levels) - star_count) // 2
for count in range(levels - 1):
    stars = "*" * star_count
    spaces = " " * spaces_count
    print(spaces + stars + spaces)
    star_count += 2
    spaces_count -= 1
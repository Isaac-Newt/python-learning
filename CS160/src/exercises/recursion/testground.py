"""Testing"""
def rec_upsidedown_triangle(levels, count):
    """Upside Down Triangle"""
    stars = "* " * count
    print(f"{stars:^{levels * 2}}")
    if count > 1:
        rec_upsidedown_triangle(levels, count - 1)

def rec_upsideup_triangle(levels, count):
    """Right Side Up Triangle"""
    stars = "* " * (levels - count)
    print(f"{stars:^{levels * 2}}")
    if count > 0:
        rec_upsideup_triangle(levels, count - 1)

def recursive_hourglass(levels, counter):
    """Recursive Hourglass"""
    if counter < (2 * levels) - 1:
        if counter < levels:
            stars = "* " * (levels - counter)
        else:
            stars = "* " * (counter - (levels - 2))
        print(f"{stars:^{levels * 2}}")
        recursive_hourglass(levels, counter + 1)

def recursive_diamond(levels, counter):
    """Recursive diamond"""
    if counter < (2 * levels) - 1:
        if counter < levels:
            stars = "* " * (counter + 1)
        else:
            stars = "* " * ((2 * - 1) - counter)
        print(f"{stars:^{levels * 2}}")
        recursive_diamond(levels, counter + 1)

# rec_upsidedown_triangle(7, 7)
# rec_upsideup_triangle(7, 6)

recursive_diamond(5, 0)
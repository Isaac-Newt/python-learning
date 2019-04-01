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


rec_upsidedown_triangle(7, 7)
rec_upsideup_triangle(7, 6)
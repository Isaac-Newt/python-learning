#!/usr/bin/env python3
"""
Recursion exercise

Isaac List - CS160
April 1, 2019
"""


def gcd(a_num: int, b_num: int) -> int:
    """Recursive GCD finder"""
    raise NotImplementedError


def hourglass_ite(levels: int) -> None:
    """Iterative hourglass"""
    star_count = levels
    for count in range(levels):
        stars = "* " * star_count
        print(f"{stars:^{levels * 2}}")
        star_count -= 1

    star_count = 2
    for count in range(levels - 1):
        stars = "* " * star_count
        print(f"{stars:^{levels * 2}}")
        star_count += 1


def diamond_ite(levels: int) -> None:
    """Iterative Diamond"""
    star_count = 1
    for count in range(levels):
        stars = "* " * star_count
        print(f"{stars:^{levels * 2}}")
        star_count += 1

    star_count = levels - 1
    for count in range(levels - 1):
        stars = "* " * (star_count)
        print(f"{stars:^{levels * 2}}")
        star_count -= 1


def hourglass_rec(levels: int, counter: int) -> None:
    """Recursive Hourglass"""
    if counter < (2 * levels) - 1:
        if counter < levels:
            stars = "* " * (levels - counter)
        else:
            stars = "* " * (counter - (levels - 2))
        print(f"{stars:^{levels * 2}}")
        hourglass_rec(levels, counter + 1)


def diamond_rec(levels: int, counter: int) -> None:
    """Recursive Diamond"""
    if counter < (2 * levels) - 1:
        if counter < levels:
            stars = "* " * (counter + 1)
        else:
            stars = "* " * ((2 * levels - 1) - counter)
        print(f"{stars:^{levels * 2}}")
        diamond_rec(levels, counter + 1)


def main():
    """Main function"""
    hourglass_ite(5)
    print()
    hourglass_rec(5, 0)
    diamond_ite(5)
    print()
    diamond_rec(5, 0)


if __name__ == "__main__":
    main()

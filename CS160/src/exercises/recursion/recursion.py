#!/usr/bin/env python3
"""Recursion exercise code template"""


def gcd(a: int, b: int) -> int:
    raise NotImplementedError


def hourglass_ite(levels: int) -> None:
    spaces_count = 0
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


def diamond_ite(levels: int) -> None:
    star_count = 1
    spaces_count = ((2 * levels) - star_count) // 2
    for count in range(levels):
        stars = "*" * star_count
        spaces = " " * spaces_count
        print(spaces + stars + spaces)
        star_count += 2
        spaces_count -= 1

    spaces_count = 1
    star_count = levels - 1
    for count in range(levels - 1):
        stars = "*" * (2 * star_count - 1)
        spaces = " " * spaces_count
        print(spaces + stars + spaces)
        star_count -= 1
        spaces_count += 1


def hourglass_rec(levels: int) -> None:
    raise NotImplementedError


def diamond_rec(levels: int) -> None:
    raise NotImplementedError


def main():
    """Main function"""
    hourglass_ite(5)
    # hourglass_rec(5)
    diamond_ite(5)
    diamond_rec(5)


if __name__ == "__main__":
    main()

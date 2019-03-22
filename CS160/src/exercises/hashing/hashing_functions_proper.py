#!/usr/bin/env python3
"""
Hashing functions

Isaac List - CS160
March 22, 2019
"""


def hash_remainder(key: int, size: int) -> int:
    """Find hash using remainder"""
    return key % size


def find_middle_two(string: str) -> str:
    """Recursive implementation"""
    if len(string) == 2:
        value = string
    else:
        value = find_middle_two(string[1:-1])
    return value


def hash_mid_sqr(key: int, size: int) -> int:
    """Find hash using mid-square method"""
    square = key * key

    # If square is an odd number of digits long
    if len(square) % 2 != 0:
        # Pretend to add a leading 0

    value = int(find_middle_two(square))

    return value % size


def hash_folding(key: int, size: int) -> int:
    """Find hash using folding method"""
    str_key = str(key)
    new_str_key = ""
    for char in str_key:
        if char.isdigit():
            new_str_key = new_str_key + char

    str_key = new_str_key

    total = 0
    # 2-digit chunks
    while len(str_key) > 2:
        key = str_key[:2]
        total += int(key)
        str_key = str_key[2:]
    # Add the last piece
    total += int(str_key)

    return total % size


def hash_str(key: str, size: int) -> int:
    """Find string hash using simple sum-of-values method"""
    total = 0
    # Add the integer value of each character
    for char in key:
        total += ord(char)

    return total % size


def hash_str_weighted(key: str, size: int) -> int:
    """Find string hash using character positions as weights"""
    total = 0
    #
    multiplier = 0
    for char in key:
        add = ord(char) * multiplier
        total += add
        multiplier += 1

    return total % size

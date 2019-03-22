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

    square = str(square)

    # If square is an odd number of digits long
    if len(square) % 2 != 0:
        # Add a leading 0
        square = "0" + str(square)

    value = int(find_middle_two(square))

    # # If square is 2 digits long
    # if len(square) == 2:
    #     value = int(square)

    # # If square is longer than two digits
    # else:
    #     # Find two middle digits
    #     while len(square) > 2:
    #         square = square[1:-1]
    #     value = int(square)

    return value % size


def hash_folding(key: int, size: int) -> int:
    """Find hash using folding method"""
    str_key = str(key)
    str_key = str_key.replace("-", "")

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
    raise NotImplementedError


def hash_str_weighted(key: str, size: int) -> int:
    """Find string hash using character positions as weights"""
    raise NotImplementedError

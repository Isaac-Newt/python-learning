#!/usr/bin/env python3
"""
Hashing functions

Isaac List - CS160
March 22, 2019
"""


def hash_remainder(key: int, size: int) -> int:
    """Find hash using remainder"""
    return key % size

def hash_mid_sqr(key: int, size: int) -> int:
    """Find hash using mid-square method"""
    square = key * key

    square = str(square)

    # If square is an odd number of digits long,
    # Make even with a leading 0
    if len(square) % 2 != 0:
        # Add a leading 0
        square = "0" + str(square)

    # If square is 2 digits long
    if len(square) == 2:
        value = int(square)

    # If square is longer than two digits
    else:
        # Find two middle digits
        while len(square) > 2:
            square = square[1:-1]
        value = int(square)
    
    return value % size


def hash_folding(key: int, size: int) -> int:
    """Find hash using folding method"""
    raise NotImplementedError


def hash_str(key: str, size: int) -> int:
    """Find string hash using simple sum-of-values method"""
    raise NotImplementedError


def hash_str_weighted(key: str, size: int) -> int:
    """Find string hash using character positions as weights"""
    raise NotImplementedError


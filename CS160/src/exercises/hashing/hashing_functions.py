#!/usr/bin/env python3
"""Hashing functions"""


def hash_remainder(key: int, size: int) -> int:
    """Find hash using remainder"""
    return key % size


def hash_mid_sqr(key: int, size: int) -> int:
    """Find hash using mid-square method"""
    square = key * key
    if len(str(square)) == 2:
        value = square
    elif len(str(square)) % 2 == 0:
        # Find two middle digits
        value = 1
    elif len(str(square)) % 2 != 0:
        # Add a leading 0
        square = "0" + str(square)
        square = int(square)
        print("square: ",square)
        # Find two middle digits
        value = 1
    
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


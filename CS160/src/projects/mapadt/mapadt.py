#!/usr/bin/env python3
"""
Implementation of the Map ADT as HashTable

Isaac List - CS160
April 1, 2019
"""


class HashTable:
    def __init__(self, size_init: int = 16):
        """Constructor"""
        self._size = size_init
        self._keys = [None] * self._size
        self._values = [None] * self._size

    def __getitem__(self, key: int):
        """__getitem__"""
        return self.get(key)

    def __setitem__(self, key: int, value):
        """__setitem__"""
        if self.__len__() == 16:
            raise Exception("Hash Table is full")
        self.put(key, value)

    def __len__(self):
        """__len__"""
        count = 0
        for item in self._keys:
            if item != None:
                count += 1
        return count

    def __contains__(self, key):
        """__contains__"""
        contained = False
        if key in self._keys:
            contained = True
        return contained

    def __str__(self):
        """__str__"""
        str_list = []
        for index in range(len(self._keys)):
            str_list.append(f"{self._keys[index]}: {self._values[index]}")
        full_string = "{" + ", ".join(str_list) + "}"
        return full_string

    def _hash(self, key: int, size: int):
        """Simple hash function"""
        return key % size

    def _rehash(self, old_hash: int, size: int, step: int = 1):
        """Simple or quadratic rehash"""
        return (old_hash + step) % size

    def put(self, key: int, value):
        """Add or update an item"""
        hashvalue = self._hash(key, len(self._keys))

        if self._keys[hashvalue] == None:
            self._keys[hashvalue] = key
            self._values[hashvalue] = value
        else:
            if self._keys[hashvalue] == key:
                self._values[hashvalue] = value
            else:
                next_key_slot = self._rehash(hashvalue, len(self._keys))
                while self._keys[next_key_slot] != None and self._keys[next_key_slot] != key:
                    next_key_slot = self._rehash(next_key_slot, len(self._keys))

                if self._keys[next_key_slot] == None:
                    self._keys[next_key_slot] = key
                    self._values[next_key_slot] = value
                else:
                    self._values[next_key_slot] = value

    def get(self, key: int):
        """Retrieve an item"""
        starting_slot = self._hash(key, len(self._keys))

        value = None
        stop = False
        found = False
        position = starting_slot

        while self._keys[position] != None and not found and not stop:
            if self._keys[position] == key:
                found = True
                value = self._values[position]
            else:
                position = self._rehash(position, len(self._keys))
                if position == starting_slot:
                    stop = True

        return value

    def keys(self):
        """Return all keys"""
        return self._keys

    def values(self):
        """Return all values"""
        return self._values

    def items(self):
        """Return all items"""
        items_list = []
        for index in range(len(keys)):
            item = (self._keys[index], self._values[index])
        return items_list


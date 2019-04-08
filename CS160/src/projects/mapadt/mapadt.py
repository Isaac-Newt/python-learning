#!/usr/bin/env python3
"""
Implementation of the Map ADT as HashTable

Isaac List - CS160
April 8, 2019
"""


class HashTable:
    """A class demonstrating the construction of a Map ADT"""
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
        if self.__len__() == self._size:
            raise Exception("Hash Table is full")
        self.put(key, value)

    def __len__(self):
        """__len__"""
        count = 0
        for item in self._keys:
            if item is not None:
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
            # key: 'value'
            str_list.append(f"{self._keys[index]}: '{self._values[index]}'")
        full_string = "{" + ", ".join(str_list) + "}"
        return full_string

    def _hash(self, key: int, size: int):
        """Simple hash function"""
        return key % size

    def _rehash(self, old_hash: int, size: int, step):
        """Simple or quadratic rehash"""
        return (old_hash + step) % size

    def put(self, key: int, value):
        """Add or update an item"""
        hashvalue = self._hash(key, self._size)

        if self._keys[hashvalue] is None:
            self._keys[hashvalue] = key
            self._values[hashvalue] = value
        else:
            if self._keys[hashvalue] == key:
                # replace existing data because same key
                self._values[hashvalue] = value
            else:
                next_key_slot = self._rehash(hashvalue, self._size, 1)
                while (
                        self._keys[next_key_slot] is not None
                        and self._keys[next_key_slot] != key
                ):
                    step = 1
                    next_key_slot = self._rehash(
                        next_key_slot, len(self._keys), (step ** 2)
                    )
                    step += 1
                # If either the slot is open or it is the same key
                if self._keys[next_key_slot] is None:
                    self._keys[next_key_slot] = key
                    self._values[next_key_slot] = value
                else:
                    self._values[next_key_slot] = value

    def get(self, key: int):
        """Retrieve an item"""
        starting_slot = self._hash(key, self._size)

        value = None
        stop = False
        found = False
        position = self._hash(key, self._size)

        while self._keys[position] is not None and not found and not stop:
            if self._keys[position] == key:
                found = True
                value = self._values[position]
            else:
                position = self._rehash(position, self._size, 1)
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
        for index in range(len(self._keys)):
            item = (self._keys[index], self._values[index])
            items_list.append(item)
        return items_list

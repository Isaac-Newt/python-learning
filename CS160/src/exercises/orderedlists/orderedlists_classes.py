#!/usr/bin/env python3
"""Ordered List classes"""

import random
import typing

random.seed(42)


class Node:
    """Node of a linked list"""

    def __init__(self, init_data: typing.Any):
        """Initializer"""
        self._data = init_data
        self._next = None

    def get_data(self):
        """Get node data"""
        return self._data

    def set_data(self, new_data: typing.Any) -> None:
        """Set node data"""
        self._data = new_data

    data = property(get_data, set_data)

    def get_next(self):
        """Get next node"""
        return self._next

    def set_next(self, new_next: object) -> None:
        """Set next node"""
        self._next = new_next

    next = property(get_next, set_next)

    def __str__(self) -> str:
        """Convert data to string"""
        return str(self._data)


class OrderedList:
    """Ordered Linked List class"""

    def __init__(self):
        """Initializer"""
        self._head = None
        self._count = 0

    def __getitem__(self, position: int):
        """Get item by its position"""
        raise NotImplementedError

    def __len__(self) -> int:
        """Get list size"""
        return self._count

    def __str__(self) -> str:
        """List as a string"""
        list_out = []
        current = self._head
        while current is not None:
            list_out.append(str(current.data))
            current = current.next
        return "[" + ", ".join(list_out) + "]"

    def is_empty(self) -> bool:
        """Check if the list is empty"""
        return self._head is None

    def size(self) -> int:
        """Get list size"""
        return self._count

    def add(self, value: typing.Any) -> None:
        """Add a new item to the list"""
        # Start at fist item in the list
        current = self._head
        previous = None
        stop_looking = False
        # If new node is "greater" than previous item, add it
        # If end of list is reached, append the item
        while current != None and not stop_looking:
            if current.get_data() > value:
                stop_looking = True
            else:
                previous = current
                current = current.get_next()
        
        # Create a new node with the data "value"
        new_node = Node(value)

        # If being put at the beginning of the list,
        # Make first item "next" and point head to new_node
        if previous == None:
            new_node.set_next(self._head)
            self._head = new_node
        # If being inserted somewhere in the middle or end,
        # Insert behind the current item, pointing new_node
        # to the current, and "previous" to new_node
        else:
            new_node.set_next(current)
            previous.set_next(new_node)
        
        # Update the count of items in the list
        self._count += 1


    def pop(self, position: int = None):
        """
        Remove at item (last one by default) and get its value

        Remove the last element if the provided position is 
        greater than the length of the list
        Raise ValueError if the list is empty
        Raise IndexError if the provided position is negative        
        """
        raise NotImplementedError

    def append(self, value: typing.Any) -> None:
        """Add a new item to the end of the list"""
        # Add the item, since that's what ya gotta do
        self.add(value)

    def insert(self, position: int, value: typing.Any) -> None:
        """Insert a new item into the list"""
        # Add the item, since that's what ya gotta do
        self.add(value)

    def search(self, value: typing.Any) -> bool:
        """Search for an item in the list"""
        current = self._head
        while current is not None:
            if current.data == value:
                return True
            if current.data > value:
                return False
            current = current.next
        return False

    def index(self, value: typing.Any) -> int:
        """Return position of an item in the list"""
        idx = 0
        current = self._head
        while current:
            if current.data == value:
                return idx
            current = current.next
            idx += 1
        # Convention to return -1 if item not found
        return -1

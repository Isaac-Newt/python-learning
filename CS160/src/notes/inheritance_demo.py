#!/usr/bin/env python3

"""Example of inheritence, with many-legged deer :)"""

# Import ability to declare abstract methods
from abc import ABC, abstractmethod

class LegError(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)


class Animal(ABC):
    # Don't want to make Animal class object
    # this prevents calling class Animal in a program
    @abstractmethod
    def __init__(self, legs_init_value):
        self._limbs = legs_init_value

    def __str__(self):
        return "animal has {} legs".format(self._limbs)

    def grow_a_limb(self):
        self._limbs = self._limbs + 1

    # Don't provide an implementation for this method
    # Instead, sub-class(es) define this (a requirement)
    #
    # i.e. every animal can eat, but it's up to each
    # class to define what/how
    @abstractmethod
    def eat(self):
        pass


class Deer(Animal):
    def __init__(self):
        super().__init__(4)

    def __str__(self):
        return "Deer has {} legs".format(self._limbs)

    def eat(self):
        return "Plants"


class Snake(Animal):
    def __init__(self)
        super().__init__(0)

    def __str__(self):
        return "Snake has {} legs".format(self._limbs)

    def grow_a_limb(self):
        raise LegError("I can't grow a leg :(")

    def eat(self):
        return "Mice"

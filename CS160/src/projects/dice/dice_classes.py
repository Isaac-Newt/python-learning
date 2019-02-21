# Isaac List - CS160 - February 20, 2019 - Die Class project

#!/usr/bin/env python3
"""
Dice game(s) simulator
"""

import random
from typing import Sequence

random.seed(42)


class Die:
    """Class Die"""

    def __init__(self, possible_values: Sequence) -> None:
        """Class Die constructor"""
        self._all_values = possible_values
        self._value = random.choice(self._all_values)

    @property
    def value(self):
        """Get the die value"""
        return self._value

    @value.setter
    def value(self, _):
        """Value property setter"""
        raise ValueError("You must roll the die to change its value")

    def __str__(self):
        """__str__ override"""
        # Print value of the dice
        return str(self._value)

    def roll(self):
        """Roll the die"""
        # Random number 1-6
        self._value = random.choice(self._all_values)
        return self._value


class FrozenDie(Die):  # subclass of Die, once rolled, cannot change
    # Every frozen die /is/ a die
    """A die that cannot be rolled"""

    def __init__(self, possible_values: Sequence) -> None:
        """Class FrozenDie constructor"""
        super().__init__(possible_values)
        self._frozen = False

    @property
    def frozen(self) -> bool:
        """Frozen property getter"""
        return self._frozen

    @frozen.setter
    def frozen(self, new_value: bool) -> None:
        """Frozen property setter"""
        self._frozen = new_value

    def roll(self):
        """Roll the die"""
        # Roll if not frozen, else return the same value
        if self._frozen is False:
            self._value = random.choice(self._all_values)


class Cup:  # does not inherit from anything, simply uses Die, FrozenDie
    """Class Cup"""

    # must have a sense of which dice is which

    def __init__(self, num_dice: int, num_sides: int = 6) -> None:
        """Class FrozenDie constructor"""
        # Takes "num_dice" number of dice, generates that many dice
        self._dice = [Die(range(1, num_sides + 1)) for _ in range(num_dice)]

    def __iter__(self):
        """Cup iterator"""
        # already done :)
        return iter(self._dice)

    def __str__(self) -> str:
        """__str__ override"""
        # print nice output
        list_of_values = []
        # This is an example of calling the __iter__ function
        for dice in self:
            list_of_values.append(dice.value)
        return f"{list_of_values}"

    def shake(self) -> None:
        """Shake a cup"""
        # roll all the dice in the "cup"
        # use a loop, iterate over objects in class cup
        for dice in self:
            dice.roll()

    def add(self, die: Die) -> None:
        """Add a die to the cup"""
        # internally, cup is a list of class "Die"
        # In this method, append a new dice to the list
        self._dice.append(die)

    def remove(self, idx: int):
        """Remove a die from the cup"""
        return self._dice.pop(idx)

    def roll(self, *args) -> None:
        """Roll specific dice"""
        # provide dice number(s) you want to roll, and roll those specific dice
        # i.e. C.roll(1, 2, 5), can be as many or as few as desired
        # Assuming dice[1] is the first die, not dice[0]
        for index in args:
            if 0 < index <= len(self._dice):
                self._dice[index - 1].roll()
        # Don't have to return self._dice, since lists are mutable, and changing it
        # within the function will change it on the "outside" too.

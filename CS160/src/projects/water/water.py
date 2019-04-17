#!/usr/bin/env python3
"""
Water jugs project

Isaac List - CS160
April 16, 2019
"""


JUG_1_MAX = 5
JUG_2_MAX = 3


class State:
    """State of the jugs"""

    def __init__(self, jug_1: int, jug_2: int):
        """__init__"""
        self._jug_1_level = jug_1
        self._jug_2_level = jug_2
        self._jug_1_limit = 5
        self._jug_2_limit = 3
        self._goal_state = 4

    def __eq__(self, other: object):
        """__eq__"""
        equal = False
        if self._jug_1_level == other._jug_1_level:
            if self._jug_2_level == other._jug_2_level:
                equal = True
        return equal

    def __str__(self):
        """__str__"""
        string_1 = f"Jug 1 has {self._jug_1_level} gallons"
        string_2 = f"Jug 2 has {self._jug_2_level} gallons"
        string_3 = f"Alltogether, {self._jug_1_level + self._jug_2_level} gallons"
        return f"{string_1}, {string_2}. {string_3}.\n"

    def clone(self):
        """Copy a state"""
        return State(self._jug_1_level, self._jug_2_level)

    def fill_jug_1(self):
        """Fill jug1 to capacity from the pump"""
        self._jug_1_level = self._jug_1_limit

    def fill_jug_2(self):
        """Fill jug2 to capacity from the pump"""
        self._jug_2_level = self._jug_2_limit

    def empty_jug_1(self):
        """Pour the water from jug1 onto the ground"""
        self._jug_1_level = 0

    def empty_jug_2(self):
        """Pour the water from jug2 onto the ground"""
        self._jug_2_level = 0

    def pour_jug_1_to_jug_2(self):
        """Pour as much water as you can from jug1 to jug2 without spilling"""
        available_space = self._jug_2_limit - self._jug_2_level
        if available_space <= self._jug_1_level:
            # if you can fill 2 with what is in 1
            amount_to_move = available_space
        else:
            # if you can empty 1 into 2
            amount_to_move = self._jug_1_level
        self._jug_1_level = self._jug_1_level - amount_to_move
        self._jug_2_level = self._jug_2_level + amount_to_move


    def pour_jug_2_to_jug_1(self):
        """Pour as much water as you can from jug2 to jug1 without spilling"""
        available_space = self._jug_1_limit - self._jug_1_level
        if available_space <= self._jug_2_level:
            # if you can fill 2 with what is in 1
            amount_to_move = available_space
        else:
            # if you can empty 1 into 2
            amount_to_move = self._jug_2_level
        self._jug_2_level = self._jug_2_level - amount_to_move
        self._jug_1_level = self._jug_1_level + amount_to_move


def search(start_state: object, goal: object, moves_lst: list):
    """Find a sequence of states"""
    moves_lst.append(start_state)

    # Fill Jug 1

    # Change the state with each option
    new_state = start_state.clone()
    new_state.fill_jug_1()
    # Decide what to do with the new state
    if new_state == goal:
        moves_lst.append(new_state)
        return
    elif new_state in moves_lst:
        pass
    else:
        search(new_state, goal, moves_lst)

    # Fill Jug 2
    
    # Change the state with each option
    new_state = start_state.clone()
    new_state.fill_jug_2()
    # Decide what to do with the new state
    if new_state == goal:
        moves_lst.append(new_state)
        return
    elif new_state in moves_lst:
        pass
    else:
        search(new_state, goal, moves_lst)

    # Empty Jug 1
    
    # Change the state with each option
    new_state = start_state.clone()
    new_state.empty_jug_1()
    # Decide what to do with the new state
    if new_state == goal:
        moves_lst.append(new_state)
        return
    elif new_state in moves_lst:
        pass
    else:
        search(new_state, goal, moves_lst)

    # Empty Jug 2
    
    # Change the state with each option
    new_state = start_state.clone()
    new_state.empty_jug_2()
    # Decide what to do with the new state
    if new_state == goal:
        moves_lst.append(new_state)
        return
    elif new_state in moves_lst:
        pass
    else:
        search(new_state, goal, moves_lst)

    # Pour jug 1 into jug 2
    
    # Change the state with each option
    new_state = start_state.clone()
    new_state.pour_jug_1_to_jug_2()
    # Decide what to do with the new state
    if new_state == goal:
        moves_lst.append(new_state)
        return
    elif new_state in moves_lst:
        pass
    else:
        search(new_state, goal, moves_lst)

    # Pour jug 2 into jug 1
    
    # Change the state with each option
    new_state = start_state.clone()
    new_state.pour_jug_2_to_jug_1()
    # Decide what to do with the new state
    if new_state == goal:
        moves_lst.append(new_state)
        return
    elif new_state in moves_lst:
        pass
    else:
        search(new_state, goal, moves_lst)

def main():
    """Main function"""
    goal = State(4, 0)
    start = State(0, 0)
    moves = []
    search(start, goal, moves)
    print(", ".join([str(s) for s in moves]))


if __name__ == "__main__":
    main()

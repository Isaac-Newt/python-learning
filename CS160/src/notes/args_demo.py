#!/usr/bin/env python3

"""Argument demo"""

# argv -> argument values
# argc -> argument count

# used to get input from system
import sys

# Make an exception, i.e. make sub-class of Python's "Exception" class
class FridayError(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

# Should not use *args with the * in a function, only as a parameter
def args_demo(*args):
    # args is a tuple
    print(args)
    # *args is also (kind of) a tuple, but an evil one. Don't use it
    print(*args)
    # You can iterate over args like any tuple
    for arg in args:
        print(arg)
    print()

def keyword_args_demo(**kwargs):
    # kwargs is a dictionary
    print(type(kwargs))
    # it prints like a dictionary -> {key: "value", key: "value"}
    print(kwargs)
    # You can access values with keys like any dictionary
    print(f"Hello {kwargs['name']}, it's {kwargs['day']}")
    # You can also iterate over it
    for key in kwargs:
        print(key, kwargs[key])
    print()

# keyword arguments must be the last thing passed into the function
def demo(name, *args, **kwargs):
    print(name)
    print(args)
    print(kwargs)
    # Example of making an exception error, can have custom message
    if kwargs["day"] == "Friday":
        raise FridayError("Let's cancel Mondays!")
    print()

def main(argv):
    print(argv)
    print(f"Hello {' '.join(argv[1:])}")
    print()
    args_demo(1, 2, 3)
    keyword_args_demo(name = "CS160", day = "Friday")
    demo("CS160", 1, 2, 3, day = 'Friday')

if __name__ == "__main__":
    # sys.argv pulls in everything typed after 
    main(sys.argv)

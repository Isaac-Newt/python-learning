#! /usr/bin/python3

class Point:
    # This describes what the class is, and any other useful info
    # Shows up as a pop-over when hovering any creation instances
    # in VSCode, so use this to help yourself in the future :)
    """
    Class Point

    x and y must be int's 
    """
    # __init__() takes "self" as well as any other desired parameters
    # "self" can technically be anything you want, but should use self
    def __init__(self, x: int, y: int):
        # 
        if type(x) is not int:
            raise TypeError
        if type(y) is not int:
            raise TypeError
        # use _x to indicate this is an internal value
        # Not a technical statement, rather a style convention
        self._x = x
        self._y = y
    

    # A Magic method :)
    # Should look up what this actually is, since it's probably important
    def __str__(self):
        return f"Point at ({self._x}, {self._y}) Got it?"


def main():
    """
    The main function, currently runs a demo
    """
    print("Point demo")
    # Create p1 as a point with x = 1, y = 6
    p1 = Point(1, 6)
    print(f"Point 1 at ({p1._x}, {p1._y})")
    # Attempt to create an invalid point
    try:
        p2 = Point("hello", [1, 2, 3])
        print(f"Point 2 at ({p2._x}, {p2._y})")
    except:
        print("Oops")


# Only run main() if file is being run directly
# If being run as a module, don't automatically run main()
if __name__ == "__main__":
    main()
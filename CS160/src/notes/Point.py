#! /usr/bin/python3


import math


class Point:
    # This describes what the class is, and any other useful info
    # Shows up as a pop-over when hovering any creation instances
    # in VSCode, so use this to help yourself in the future :)
    """
    Class Point

    This class provides methods for building 2D points, and performing
    operations with these points

    x and y must be int's
    """
    # __init__() takes "self" as well as any other desired parameters
    # "self" can technically be anything you want, but should use self

    def __init__(self, x: int, y: int):
        """Create a point"""
        if type(x) is not int:
            raise TypeError
        if type(y) is not int:
            raise TypeError
        # use _x to indicate this is an internal value
        # Not a technical statement, rather a style convention
        # Should not be accessed by anything outside of the class!
        self._x = x
        self._y = y

    """
    Define Getters and Setters
    """

    # Call these with p1.get_x()
    def get_x(self):
        """Get point's x value"""
        return self._x

    # Call these with p1.set_x(10)
    def set_x(self, new_value):
        """Set point's x value"""
        self._x = new_value

    # Can call with p1.x --> int, p1.x =
    x = property(get_x, set_x)

    # Does for y what the above property() does for x
    @property
    def y(self):
        """Get y value of point"""
        return self._y

    @y.setter
    def y(self, new_value):
        """Set y value of point"""
        self._y = new_value

    # __str__ vs __repr__:
    #
    # __str__ is supposed to be human readable, whereas
    # __repr__ may be more useful to the machine
    #
    # If you print an object itself, __str__ is called.
    # i.e. print(p1) == print(str(p1))
    #
    # If you print a list of objects, __repr__ is called.
    # i.e. print(my_list_of_points) == print(repr(p1), repr(p2))

    # A Magic method :)
    # Express an object as a string
    def __str__(self):
        """Express the point as a string"""
        return f"Point at ({self._x}, {self._y}) Got it?"

    # Express object as it would have been created
    # i.e. Point(1, 6)
    def __repr__(self):
        """Returns the way the object is created"""
        return f"Point({self._x}, {self._y})"

    # Define how to determine if two object instances are equal
    # Python default is comparing memory location (pointless) :)
    def __eq__(self, other):
        """
        Define how to compare two points
        Arguments for current point and for other point
        Call with "==" operator
        """
        # Points are the same if x and y values are the same
        return self._x == other._x and self._y == other._y

    # Here you should also define __lt__ (less than, <), __le__
    # (less than or equal to, <=), __add__ (addition, +), and
    # __mult__ (multiplication, *)
    #
    # Generally don't need to have >, >=, -, or /, because convention
    # if you use > and only have __lt__ defined, python will get it right
    #
    # For example, this will work to catch > or < operators
    def __lt__(self, other):
        """"A point is less than another if it is closer to (0, 0)"""
        center = Point(0, 0)
        return self.distance(center) < other.distance(center)

    """Now we define non-magic functions"""

    # Call with p1.distance(p2)
    def distance(self, other):
        """Find distance between two points"""
        # must import math for this silly
        return math.sqrt((self._x - other._x) ** 2 + (self._y - other._y) ** 2)


class Point3D(Point):  # put class from which sub-class inherits in the ()'s
    """
    This class extends the Point class with 3D capabilities

    It is a sub-class of the Point super class, and inherits from it
    """

    def __init__(self, x_init_value, y_init_value, z_init_value):
        """Create a 3D Point"""
        # Call __init__() of super class to build (x, y) of point
        super().__init__(x_init_value, y_init_value)
        self._z = z_init_value

    @property
    def z(self):
        return self._z

    def __str__(self):
        """String representation of the Point3D Object"""
        return f"({self.x}, {self.y}, {self.z})"


def main():
    """
    The main function, currently runs a demo
    """

    print("Point3D demo")
    # p3 = Point3D（1， 2, 3）
    # This will return a valid output as if called with
    # Point() even if no new properties in Point3D
    print(p3)

    print("Point demo")

    """Point Creation"""
    # Create p1 as a point with x = 1, y = 6
    p1 = Point(1, 6)
    print(f"Point 1 at ({p1._x}, {p1._y})")
    # Attempt to create an invalid point
    try:
        p2 = Point("hello", [1, 2, 3])
        print(f"Point 2 at ({p2._x}, {p2._y})")
    except:
        print("Oops")

    """Point Representation/Visualization"""
    # Attempt to print a list of p1 and p2
    all_my_points = [p1]
    # will return useless garbage unless you define __repr__
    print(all_my_points)
    # Attempt to compare points, must define how to do this
    # in __eq__()
    p4 = Point(1, 6)
    print(p1 == p4)


# Only run main() if file is being run directly
# If being run as a module, don't automatically run main()
if __name__ == "__main__":
    main()

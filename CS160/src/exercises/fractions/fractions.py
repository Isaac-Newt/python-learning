#! python3.7
"""
Implementation of the class Fraction
"""


def gcd(num_a: int, num_b: int) -> int:
    """
    Greatest Common Denominator of two integers

    Helper function to simplify fractions
    """
    while num_a % num_b:
        num_a, num_b = num_b, num_a % num_b
    return num_b


class Fraction:
    """Class Fraction

    Takes two parameters: numerator and denominator

    Both Numerator and Denominator must be int's
    """

    def __init__(self, numerator: int, denominator: int):
        """
        Defines fraction components
        """
        if type(numerator) == int and type(denominator) == int:
            self._num = numerator
            self._den = denominator
        else:
            if type(numerator) != int:
                raise TypeError("Numerator must be an integer number")
            if type(denominator) != int:
                raise TypeError("Denominator must be an integer number")

    def get_numerator(self) -> int:
        """Return fraction numerator"""
        return self._num

    numerator = property(get_numerator) # use with self.numerator

    def get_denominator(self) -> int:
        """Return fraction denominator"""
        return self._den

    denominator = property(get_denominator) # use with self.denominator

    def __str__(self) -> str:
        """
        Object as a string

        To Do: Use numerator/denominator "properties" rather than self._x
        clean up gcd usage, it looks kinda like garbage right now tbh :(
        """
        greatest_common_denominator = gcd(self._num, self._den)
        numerator = self.numerator // greatest_common_denominator
        denominator = self.denominator // greatest_common_denominator
        if numerator < denominator:
            return f"{numerator}/{denominator}"
        elif numerator == denominator:
            return "1"
        else: # i.e. numerator > denominator
            integer = numerator - denominator
            numerator = int(numerator - (integer * denominator))
            integer = str(integer)
            return f"{integer} {numerator}/{denominator}"


    def __repr__(self) -> str:
        """Object representation"""
        # I guess this is supposed to be akin to "Fraction(num, den)"?
        greatest_common_denominator = gcd(self.numerator, self.denominator)
        numerator = self.numerator // greatest_common_denominator
        denominator = self.denominator // greatest_common_denominator
        return f"Fraction({numerator}, {denominator})"

    def __eq__(self, other: object) -> bool:
        """Equality comparison"""
        raise NotImplementedError

    def __gt__(self, other: object) -> bool:
        """Greater than comparison"""
        raise NotImplementedError_den

    def __ge__(self, other: object) -> bool:
        """Greater than or equal comparison"""
        if isinstance(other, Fraction):
            return (
                self.numerator / self.denominator >= other.numerator / other.denominator
            )
        raise TypeError("Can only compare Fractions")

    def __add__(self, other: object) -> object:
        """Add two fractions"""
        raise NotImplementedError

    def __sub__(self, other: object) -> object:
        """Subtract two fractions"""
        raise NotImplementedError

    def __mul__(self, other: object) -> object:
        """Multiply two fractions"""
        raise NotImplementedError

    def __truediv__(self, other: object) -> object:
        """Divide two fractions"""
        raise NotImplementedError


def main():
    """Main function"""
    print("Working with Classes")
    fraction1 = Fraction(10, 4)
    print(f"Fraction 1 is {fraction1}")
    fraction2 = Fraction(10, 12)
    print(f"Fraction 2 is {fraction2}")
    fraction3 = Fraction(3, 4)
    print(f"Fraction 3 is {fraction3}")
    print(f"Its id is {id(fraction3)}")
    fraction4 = Fraction(3, 4)
    print(f"Fraction 4 is {fraction4}")
    print(f"Its id is {id(fraction4)}")

    print("Comparison")
    if fraction3 == fraction4:
        print(f"{fraction3} and {fraction4} are equal!")
    else:
        print(f"{fraction3} and {fraction4} are different!")

    print(f"{fraction1} + {fraction2} = {fraction1 + fraction2}")


if __name__ == "__main__":
    main()

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
        if isinstance(numerator, int) and isinstance(denominator, int):
            # find greatest common denominator
            greatest_common_denominator = gcd(numerator, denominator)
            self._num = numerator // greatest_common_denominator
            self._den = denominator // greatest_common_denominator
        else:
            if not isinstance(numerator, int):
                raise TypeError("Numerator must be an integer number")
            if not isinstance(denominator, int):
                raise TypeError("Denominator must be an integer number")

    def get_numerator(self) -> int:
        """Return fraction numerator"""
        return self._num

    numerator = property(get_numerator)  # use with self.numerator

    def get_denominator(self) -> int:
        """Return fraction denominator"""
        return self._den

    denominator = property(get_denominator)  # use with self.denominator

    def __str__(self) -> str:
        """
        Object as a string
        """
        if self.numerator <= self.denominator:
            return f"{self.numerator}/{self.denominator}"
        if self.numerator > self.denominator:
            integer = self.numerator - self.denominator
            numerator = int(self.numerator - (integer * self.denominator))
            integer = str(integer)
            return f"{integer} {numerator}/{self.denominator}"

    def __repr__(self) -> str:
        """Object representation"""
        return f"Fraction({self.numerator}, {self.denominator})"

    def __eq__(self, other: object) -> bool:
        """Equality comparison"""
        # equal if num1 * den2 == num2 * den1
        if isinstance(other, Fraction):
            if (self.numerator * other.denominator) == (
                self.denominator * other.numerator
            ):
                return True
            return False
        raise TypeError("Can only compare Fractions")

    def __gt__(self, other: object) -> bool:
        """Greater than comparison"""
        if isinstance(other, Fraction):
            # find common denominator, compare numerators
            numerator1 = self.numerator * other.denominator
            numerator2 = other.numerator * self.denominator
            return numerator1 > numerator2
        raise TypeError("Can only compare Fractions")

    def __ge__(self, other: object) -> bool:
        """Greater than or equal comparison"""
        if isinstance(other, Fraction):
            return (
                self.numerator / self.denominator >= other.numerator / other.denominator
            )
        raise TypeError("Can only compare Fractions")

    def __add__(self, other: object) -> object:
        """Add two fractions"""
        # Find common denominator, add numerators
        if isinstance(other, Fraction):
            numerator1 = self.numerator * other.denominator
            numerator2 = other.numerator * self.denominator
            final_numerator = numerator1 + numerator2
            final_denominator = self.denominator * other.denominator
            return Fraction(final_numerator, final_denominator)
        raise TypeError("Can only add two Fractions")

    def __sub__(self, other: object) -> object:
        """Subtract two fractions"""
        if isinstance(other, Fraction):
            numerator1 = self.numerator * other.denominator
            numerator2 = other.numerator * self.denominator
            final_numerator = numerator1 - numerator2
            final_denominator = self.denominator * other.denominator
            return Fraction(final_numerator, final_denominator)
        raise TypeError("Can only subtract two Fractions")

    def __mul__(self, other: object) -> object:
        """Multiply two fractions"""
        if isinstance(other, Fraction):
            numerator = self.numerator * other.numerator
            denominator = self.denominator * other.denominator
            return Fraction(numerator, denominator)
        raise TypeError("Can only multiply two Fractions")

    def __truediv__(self, other: object) -> object:
        """Divide two fractions"""
        if isinstance(other, Fraction):
            # Multiply by the recipricol
            numerator2 = other.denominator
            denominator2 = other.numerator
            # Utilize multiplication function
            return self * Fraction(numerator2, denominator2)
        raise TypeError("Can only divide two Fractions")


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

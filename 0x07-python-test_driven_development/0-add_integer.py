#!/usr/bin/python3
"""Module for add integers"""


def add_integer(a, b=98):
    """
    Add to integers

    Args:
        a: first num
        b: second num

    Raises:
        TypeError: if a or b not int or float

    Returns:
        sum
    """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest

    doctest.testfile("tests/0-add_integer.txt")

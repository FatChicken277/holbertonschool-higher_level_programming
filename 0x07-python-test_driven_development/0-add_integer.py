#!/usr/bin/python3

"""This module contains a function that returns
    the addition of two integers.
"""


def add_integer(a, b=98):
    """Adds two integers.

    Arguments:
        a (int) -- first argument must be an integer or float.
        b (int) -- seccond argument must be an integer or float.
                    default value: 98
    Raises:
        TypeError: var must be an integer.
        TypeError: var must be an integer.

    Returns:
        int -- returns the addition of a and b.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)

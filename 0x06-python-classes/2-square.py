#!/usr/bin/python3

"""Create and define the class "Square".

This module creates an class called "Square" that defines a square.

  Typical usage example:

  var = Square()
"""


class Square:
    """Defines a Square.

    Defines a square and its values subject to certain conditions.

    Attributes:
        __size: size of the square.
    """

    def __init__(self, size=0):
        """Inits Square with a size subject to certain conditions."""
        if size != int(size):
            raise ValueError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

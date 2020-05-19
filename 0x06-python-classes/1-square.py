#!/usr/bin/python3

"""Create and define the class "Square".

This module creates an class called "Square" that defines a square.

  Typical usage example:

  var = Square()
"""


class Square:
    """Define a square.

    Define a square by size.

    Attributes:
        __size: size of the square.
    """

    def __init__(self, size):
        """Inits Square with a size."""
        self.__size = size

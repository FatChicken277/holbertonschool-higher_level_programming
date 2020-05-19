#!/usr/bin/python3

"""Create and define the class "Square".

This module creates an class called "Square" that defines a square.

  Typical usage example:

  var = Square()
"""


class Square:
    """Define a square.

    Define a square by size and value.

    Attributes:
        __size: size of the square.
        value: value of the square.
    """
    __size = None

    def __init__(self, value):
        """Inits Square with a value."""
        self.value = value

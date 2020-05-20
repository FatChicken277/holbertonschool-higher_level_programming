#!/usr/bin/python3

"""Create and define the class "Square".

This module creates an class called "Square" that defines a square.

  Typical usage example:

  var = Square() or var = Square(arg)
"""


class Square:
    """Defines a Square.

    Defines a square and its values subject to certain conditions.

    Attributes:
        __size: size of the square.
    """

    def __init__(self, size=0):
        """Inits Square."""
        self.__size = size

    @property
    def size(self):
        """Returns Square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets Square with a size subject to certain conditions."""
        if type(value) is not int:
            raise ValueError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current square area."""
        return self.__size * self.__size

    def my_print(self):
        """that prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        for i in range(self.__size):
                print("#" * self.__size)

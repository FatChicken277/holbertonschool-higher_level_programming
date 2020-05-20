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
        __position: position of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Inits Square."""
        if type(size) is not int:
            raise ValueError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if type(position) is not tuple or type(position[0]) is not int\
                or type(position[1]) is not int\
                or position[0] < 0 or position[1] < 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = position

    @property
    def size(self):
        """Returns Square size"""
        return self.__size

    @property
    def position(self):
        """Returns Square position"""
        return self.__position

    @size.setter
    def size(self, value):
        """Sets Square with a size subject to certain conditions."""
        if type(value) is not int:
            raise ValueError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """Sets Square with a position subject to certain conditions."""
        if type(value) is not tuple or type(value[0]) is not int\
                or type(value[1]) is not int or value[0] < 0 or value[1] < 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area."""
        return self.__size * self.__size

    def my_print(self):
        """that prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        if self.__position[1] != 0:
            print("" * self.__position[1])
        for i in range(self.__size):
            if self.__position[0] != 0:
                print(" " * self.__position[0], end="")
            print("#" * self.__size)

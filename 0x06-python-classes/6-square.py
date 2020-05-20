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
        """Inits Square.

        Keyword Arguments:
            size {Int} -- size (default: {0})
            position {Tuple} -- position (default: {(0, 0)})

        Raises:
            TypeError: size must be an integer
            ValueError: size must be >= 0
            TypeError: position must be a tuple of 2 positive integers
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        if type(position) is not tuple or len(position) is not 2\
                or type(position[0]) is not int\
                or type(position[1]) is not int\
                or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    @property
    def size(self):
        """Returns Square size.

        Returns:
            Int -- size.
        """
        return self.__size

    @property
    def position(self):
        """Returns Square position.

        Returns:
            Int -- Position.
        """
        return self.__position

    @size.setter
    def size(self, value):
        """Sets Square with a size subject to certain conditions.

        Arguments:
            value {Int} -- size.

        Raises:
            TypeError: size must be an integer.
            ValueError: size must be >= 0.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @position.setter
    def position(self, value):
        """Sets Square with a position subject to certain conditions.

        Arguments:
            value {Int} -- position.

        Raises:
            TypeError: position must be a tuple of 2 positive integers.
        """
        if type(value) is not tuple or len(value) is not 2\
                or type(value[0]) is not int or type(value[1]) is not int\
                or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Returns the area of the square.

        Returns:
            Int -- area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """that prints in stdout the square with the character #.
        """
        if self.__size == 0:
            print()
            return
        if self.__position == (0, 0):
            for i in range(self.__size):
                print("#" * self.__size)
        else:
            if self.__position[1] > 0:
                print("\n" * self.__position[1], end="")
            for i in range(self.__size):
                if self.__position[0] != 0:
                    print(" " * self.__position[0], end="")
                print("#" * self.__size)

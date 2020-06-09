#!/usr/bin/python3
"""This module contains a class Square that inherits from Rectangle.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square that inherits from Rectangle.

    Args:
        Rectangle: father class.
    """
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor that sets the instance attributes.

        Args:
            size (int): size value.
            x (int, 0): x value. Defaults to 0.
            y (int, 0): y value. Defaults to 0.
            id (int), None): id value. Defaults to None.
        """
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns "[Square] (<id>) <x>/<y> - <size>"

        Returns:
            str: "[Square] (<id>) <x>/<y> - <size>"
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Getter of the square size.

        Returns:
            int: size value.
        """
        return self.width

    @size.setter
    def size(self, value):
        """Setter of the square size.

        Args:
            value (int): square new size.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns a key/value argument to attributes.
        """
        l1 = ["id", "size", "x", "y"]
        if args:
            for idx, val in enumerate(args):
                setattr(self, l1[idx], val)
        else:
            for key, val in kwargs.items():
                if key in l1:
                    setattr(self, key, val)

    def to_dictionary(self):
        """Returns the dictionary representation of a Square.

        Returns:
            dict: dictionary representation of a Square.
        """
        new = {}
        for key, val in self.__dict__.items():
            if key.split("_")[-1] == "height" or key.split("_")[-1] == "width":
                new["size"] = val
            else:
                new[key.split("_")[-1]] = val
        return new

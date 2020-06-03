#!/usr/bin/python3
"""This module contains a class MyInt that inherits from int
"""


class MyInt(int):
    """class MyInt that inherits from int

    Arguments:
        int -- int
    """

    def __eq__(self, other):
        """[summary]

        Arguments:
            other -- other

        Returns:
            not equal
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """[summary]

        Arguments:
            other -- other

        Returns:
            equal
        """
        return super().__eq__(other)

#!/usr/bin/python3
"""this module provides a function that returns
 a the list of available attributes and methods of an object.
"""


def lookup(obj):
    """returns a the list of available attributes
     and methods of an object.

    Arguments:
        obj (object) -- object.

    Returns:
        list -- attributes and methods of an object.
    """
    return dir(obj)

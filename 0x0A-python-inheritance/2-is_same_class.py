#!/usr/bin/python3
"""This module contains a function that returns True if
 the object is exactly an instance of the specified class ;
 otherwise False.
"""


def is_same_class(obj, a_class):
    """function that returns True if
    the object is exactly an instance of the specified class ;
    otherwise False.

    Arguments:
        obj (obj) -- object
        a_class (cls) -- class

    Returns:
        boolean -- True / False
    """
    return type(obj) is a_class

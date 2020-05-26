#!/usr/bin/python3

"""prevents the user from dynamically creating new
    instance attributes, except if the new instance attribute
    is called first_name.
"""


class LockedClass:
    """Prevents the user from dynamically
        creating new instance attributes.
    """
    __slots__ = 'first_name'

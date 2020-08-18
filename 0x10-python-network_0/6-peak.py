#!/usr/bin/python3
"""This module contains a function that finds a peak in a
    list of unsorted integers.
"""


def find_peak(list_of_integers):
    """That finds a peak in a list of unsorted integers.
    """
    if list_of_integers:
        return max(list_of_integers)

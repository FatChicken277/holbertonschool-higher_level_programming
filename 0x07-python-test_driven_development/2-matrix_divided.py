#!/usr/bin/python3

"""This module has a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix.

    Arguments:
        matrix (list) -- matrix of lists.
        div (int/float) -- divisor.

    Raises:
        TypeError: matrix must be a matrix (list of lists) of integers/floats.
        TypeError: div must be a numbe.
        ZeroDivisionError: division by zero.
        TypeError: matrix must be a matrix (list of lists) of integers/floats.
        TypeError: Each row of the matrix must have the same size.
        TypeError: matrix must be a matrix (list of lists) of integers/floats.

    Returns:
        list -- returns a new matrix with all divisions
    """
    if type(matrix) is not list or len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    lon = []
    array = []
    for items in matrix:
        if type(items) is not list or len(items) == 0:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if lon == []:
            lon.append(len(items))
        if lon[-1] == len(items):
            lon.append(len(items))
        else:
            raise TypeError("Each row of the matrix must have the same size")
        for item in items:
            if type(item) not in [int, float]:
                raise TypeError("matrix must be a matrix\
 (list of lists) of integers/floats")
        array.append([round(x / div, 2) for x in items])
    return array

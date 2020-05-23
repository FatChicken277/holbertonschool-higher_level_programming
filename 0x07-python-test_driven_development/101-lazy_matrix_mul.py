#!/usr/bin/python3
"""This module contains a function that multiplies 2 matrices
    by using the module NumPy
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    """multiplies 2 matrices by using the module NumPy.
    """
    result = numpy.dot(m_a, m_b)
    return result

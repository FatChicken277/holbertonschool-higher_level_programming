#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return [[y*y for y in matrix[x]] for x in range(len(matrix))]

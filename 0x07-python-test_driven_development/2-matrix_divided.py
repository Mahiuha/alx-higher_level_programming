#!/usr/bin/python3
"""
    matrix division module
"""


def matrix_divided(matrix, div):
    """ Takes a matrix and divides the values by 'div'.

    Args:
        matrix (:obj:'list' of :obj:'list'): lists of lists of integers/floats.
        div (int or float): The divisor.
    """
    row_len = -1
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div is 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) is not list or len(matrix) is 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/"
                        "floats")

    new_matrix = []
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of "
                            "integers/floats")
        if row_len is -1:
            row_len = len(row)
            if row_len is 0:
                raise TypeError("matrix must be a matrix (list of lists) of "
                                "integers/floats")
        else:
            if row_len is not len(row):
                raise TypeError("Each row of the matrix must have the same "
                                "size")
        new_row = []
        for ele in row:
            if type(ele) is int or type(ele) is float:
                new_row.append(round(ele / div, 2))
            else:
                raise TypeError("matrix must be a matrix (list of lists) of "
                                "integers/floats")
        new_matrix.append(new_row)
    return new_matrix

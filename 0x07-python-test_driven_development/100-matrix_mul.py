#!/usr/bin/python3
"""
    Module containing matrix multiplication.
"""


def matrix_mul(m_a, m_b):
    """ Multiplies two matrices. Validation of matrices must be done in the
        stated order.

    Args:
        m_a (:obj:`list' of :obj:`list` of int or float): List of lists of
            integers or floats.
        m_b (:obj:`list` of :obj:`list` of int or float): List of lists of
            integers or floats.

    Returns:
        :obj:`list` of :obj:`list` of int or float: Product of two matrices.
    """

    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    a_col_len = 0
    a_row_len = None
    a_matrix = True
    a_i_or_f = True
    a_rect = True
    for row in m_a:
        if type(row) is not list:
            a_matrix = False
            break
        for x in row:
            if type(x) is not int and type(x) is not float:
                a_i_or_f = False
        if a_row_len is not None:
            if a_row_len != len(row):
                a_rect = False
        else:
            a_row_len = len(row)
        a_col_len += 1

    b_col_len = 0
    b_row_len = None
    b_matrix = True
    b_i_or_f = True
    b_rect = True
    for row in m_b:
        if type(row) is not list:
            b_matrix = False
            break
        for x in row:
            if type(x) is not int and type(x) is not float:
                b_i_or_f = False
        if b_row_len is not None:
            if b_row_len != len(row):
                b_rect = False
        else:
            b_row_len = len(row)
        b_col_len += 1

    if not a_matrix:
        raise TypeError("m_a must be a list of lists")

    if not b_matrix:
        raise TypeError("m_b must be a list of lists")

    if a_col_len is 0 or (a_row_len is 0 and a_rect):
        raise ValueError("m_a can't be empty")

    if b_col_len is 0 or (b_row_len is 0 and b_rect):
        raise ValueError("m_b can't be empty")

    if not a_i_or_f:
        raise TypeError("m_a should contain only integers or floats")

    if not b_i_or_f:
        raise TypeError("m_b should contain only integers or floats")

    if not a_rect:
        raise TypeError("each row of m_a must should be of the same size")

    if not b_rect:
        raise TypeError("each row of m_b must should be of the same size")

    if a_row_len != b_col_len:
        raise ValueError("m_a and m_b can't be multiplied")

    new_matrix = []
    for a_cdx in range(a_col_len):
        new_row = []
        for rdx in range(b_row_len):
            total = 0
            for cdx in range(b_col_len):
                total += m_b[cdx][rdx] * m_a[a_cdx][cdx]
            new_row.append(total)
        new_matrix.append(new_row)

    return new_matrix

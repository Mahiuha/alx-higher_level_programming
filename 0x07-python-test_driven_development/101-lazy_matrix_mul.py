#!/usr/bin/python3
"""
    Module containing ``lazy_matrix_mul`` function
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
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

    return np.matmul(m_a, m_b)

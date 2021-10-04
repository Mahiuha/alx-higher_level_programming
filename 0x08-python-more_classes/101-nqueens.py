#!/usr/bin/python3
"""
    Module containing functions to search for solutions to N-queens problem.
"""


def all_possible(n=4):
    """ Function to find all possible solutions by placing the first queen on
        the first row, with different column positions starting from 2nd
        column to 2nd to last column.
        Args:
            n (int): The size of the chess board, but also the number of queens
                to place on the board.
    """

    for i in range(n):
        matrix = []
        matrix.append([0, i])
        col = [z for z in range(n)]
        col.remove(i)
        recur_bt(matrix, 1, col, n)


def recur_bt(matrix, row, col, n):
    """
        Recursive backtrack function. Test remaining possible positions using
        `row` and `col` values in order to place another queen on the board.
        Base case, either the length of `matrix` is the same as `n` (all queens
        have been placed in non threatening positions) or all possible
        combinations of `row` and `col` with the current matrix yields no
        solution.
        Args:
            matrix (:obj:`list` of :obj:`list` or int): A matrix list of lists
                representing the positions of queens placed on the board.
            row (:obj:`list` of int): Possible row positions the remaining
                queens can be placed on.
            col (:obj:`list` of int): Possible column positions the remaining
                queens can be placed on.
            n (int): The size of the board, but also the number of queens that
                can fit.
        Returns:
            A list of lists which is a solution, or None if the current members
            of the matrix lead to a dead end.
    """
    if len(matrix) is n:
        return matrix

    if row:
        i = row
        for j in col:
                if (not bot_right(matrix, i + 1, j + 1, n) or
                    not bot_left(matrix, i + 1, j - 1, n) or
                    not top_left(matrix, i - 1, j - 1, n) or
                        not top_right(matrix, i - 1, j + 1, n)):
                        continue
                matrix.append([i, j])
                new_col = list(col)
                new_col.remove(j)
                new_matrix = recur_bt(matrix, row + 1, new_col, n)
                if new_matrix is not None:
                    print(matrix)
                matrix.remove([i, j])
    return None


def bot_right(matrix, y, x, n):
    """
        Function to test if there are any queens on the bottom right diagonal.
        Args:
            matrix (:obj:`list` of :obj:`list` or int): A matrix list of lists
                representing the positions of queens placed on the board.
            y (int): "row" or y co-ordinate.
                queens can be placed on.
            x (int): "column" or x co-ordinate.
            n (int): The size of the board.
        Returns:
            True if no queens exist on the bottom right diagonal otherwise
            False.
    """
    while y < n and x < n:
        if [y, x] in matrix:
            return False
        else:
            y += 1
            x += 1
    return True


def bot_left(matrix, y, x, n):
    """
        Function to test if there are any queens on the bottom left diagonal.
        Args:
            matrix (:obj:`list` of :obj:`list` or int): A matrix list of lists
                representing the positions of queens placed on the board.
            y (int): "row" or y co-ordinate.
                queens can be placed on.
            x (int): "column" or x co-ordinate.
            n (int): The size of the board.
        Returns:
            True if no queens exist on the bottom left diagonal otherwise
            False.
    """
    while y < n and x >= 0:
        if [y, x] in matrix:
            return False
        else:
            y += 1
            x -= 1
    return True


def top_left(matrix, y, x, n):
    """
        Function to test if there are any queens on the top left diagonal.
        Args:
            matrix (:obj:`list` of :obj:`list` or int): A matrix list of lists
                representing the positions of queens placed on the board.
            y (int): "row" or y co-ordinate.
                queens can be placed on.
            x (int): "column" or x co-ordinate.
            n (int): The size of the board.
        Returns:
            True if no queens exist on the top left diagonal otherwise False.
    """
    while y >= 0 and x >= 0:
        if [y, x] in matrix:
            return False
        else:
            y -= 1
            x -= 1
    return True


def top_right(matrix, y, x, n):
    """
        Function to test if there are any queens on the top right diagonal.
        Args:
            matrix (:obj:`list` of :obj:`list` or int): A matrix list of lists
                representing the positions of queens placed on the board.
            y (int): "row" or y co-ordinate.
                queens can be placed on.
            x (int): "column" or x co-ordinate.
            n (int): The size of the board.
        Returns:
            True if no queens exist on the top right diagonal otherwise False.
    """
    while y >= 0 and x < n:
        if [y, x] in matrix:
            return False
        else:
            y -= 1
            x += 1
    return True

if __name__ == "__main__":
    from sys import argv
    if len(argv) is not 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(argv[1])
    except:
        print("N must be a number")
        exit(1)
    if n < 4:
        print("N must be at least 4")
        exit(1)

    all_possible(n)

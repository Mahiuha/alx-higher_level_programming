The ``2-matrix_divided`` module
======================

Using ``matrix_divided``
-------------------

Import ``matrix_divided`` from the ``2-matrix_divided`` module:

	>>> matrix_divided = __import__('2-matrix_divided').matrix_divided

Test div as non integer/float:

	>>> matrix = [[1, 2, 3], [4, 5, 6]]
	>>> matrix_divided(matrix, "string")
	Traceback (most recent call last):
	TypeError: div must be a number

Test div as 0:

	>>> matrix = [[1, 2, 3], [4, 5, 6]]
	>>> matrix_divided(matrix, 0)
	Traceback (most recent call last):
	ZeroDivisionError: division by zero

Test non list argument:

	>>> matrix = "Not a matrix"
	>>> matrix_divided(matrix, 2)
	Traceback (most recent call last):
	TypeError: matrix must be a matrix (list of lists) of integers/floats

Test empty list:

	>>> matrix = []
	>>> matrix_divided(matrix, 2)
	Traceback (most recent call last):
	TypeError: matrix must be a matrix (list of lists) of integers/floats

Test list containing non list elements:

	>>> matrix = ["Not", "list", 4]
	>>> matrix_divided(matrix, 2)
	Traceback (most recent call last):
	TypeError: matrix must be a matrix (list of lists) of integers/floats

Test list containing lists with no elements:

	>>> matrix = [[], []]
	>>> matrix_divided(matrix, 2)
	Traceback (most recent call last):
	TypeError: matrix must be a matrix (list of lists) of integers/floats

Test list containing lists with varying amount of elements:

	>>> matrix = [[1, 3], [1]]
	>>> matrix_divided(matrix, 2)
	Traceback (most recent call last):
	TypeError: Each row of the matrix must have the same size

Test list containing lists with non integer/float elements:

	>>> matrix = [["not", "a"], ["integer", "float"]]
	>>> matrix_divided(matrix, 2)
	Traceback (most recent call last):
	TypeError: matrix must be a matrix (list of lists) of integers/floats

Test list containing lists with just integers:

	>>> matrix = [[1, 2, 3], [4, 5, 6]]
	>>> matrix_divided(matrix, 3)
	[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]

Test list containing lists with just floats:

	>>> matrix = [[1.3, 2.5, 3.4], [4.3, 5.8, 6.9]]
	>>> matrix_divided(matrix, 3)
	[[0.43, 0.83, 1.13], [1.43, 1.93, 2.3]]

Test with overflow

	>>> matrix = [[1, 2, 3]]
	>>> matrix_divided(matrix, 3.0 ** 1024)
	... # doctest: +ELLIPSIS
	Traceback (most recent call last):
	OverflowError: ...

	>>> matrix = [[1., 2., 3.]]
	>>> matrix_divided(matrix, 3.0 ** 1024)
	... # doctest: +ELLIPSIS
	Traceback (most recent call last):
	OverflowError: ...

Test with div being float('inf'):

	>>> matrix = [[1, 2, 3,]]
	>>> matrix_divided(matrix, float('inf'))
	[[0.0, 0.0, 0.0]]

	>>> matrix = [[1.1, 2.2, 3.3,]]
	>>> matrix_divided(matrix, float('inf'))
	[[0.0, 0.0, 0.0]]


Test list containing lists with floats/integers:

        >>> matrix = [[1.3, 2, 3.4], [4, 5.8, 6]]
	>>> matrix_divided(matrix, 3)
	[[0.43, 0.67, 1.13], [1.33, 1.93, 2.0]]

Test list containing one list:

	>>> matrix = [[1, 2, 3]]
        >>> matrix_divided(matrix, 3)
	[[0.33, 0.67, 1.0]]

Test with no arguments:

	>>> matrix_divided()
	Traceback (most recent call last):
	TypeError: matrix_divided() missing 2 required positional arguments: 'matrix' and 'div'

Test with only one argument:

	>>> matrix_divided(matrix)
	Traceback (most recent call last):
	TypeError: matrix_divided() missing 1 required positional argument: 'div'

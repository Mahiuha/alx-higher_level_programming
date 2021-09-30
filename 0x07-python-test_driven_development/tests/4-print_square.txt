The ``4-print_square`` module
======================

Using ``print_square``
-------------------

Import ``print_square`` from the ``4-print_square`` module:

	>>> print_square = __import__('4-print_square').print_square

Test argument as integer >= 0:

	>>> print_square(0)

	>>> print_square(4)
	####
	####
	####
	####

	>>> print_square(10)
	##########
	##########
	##########
	##########
	##########
	##########
	##########
	##########
	##########
	##########

Test argument as integer < 0:

	>>> print_square(-4)
	Traceback (most recent call last):
	ValueError: size must be >= 0

Test argument as non integer:

	>>> print_square("Zero")
	Traceback (most recent call last):
	TypeError: size must be an integer

Test no argument as non integer:

	>>> print_square()
	Traceback (most recent call last):
	TypeError: print_square() missing 1 required positional argument: 'size'

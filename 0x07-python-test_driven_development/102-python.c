#include "Python.h"
#include <stdio.h>

void print_python_string(PyObject *p);

/**
 * print_python_string - Checks if the object is a Python bytes object. If so
 * print the size, attempt to print it as a string and the first 10 bytes at
 * most in hexadecimal.
 *
 * @p: Pointer to a Python object.
 *
 * Return: void.
 */
void print_python_string(PyObject *p)
{
	Py_ssize_t p_len;
	char *str;

	printf("[.] string object info\n");
	if (PyUnicode_Check(p))
	{
		p_len = PyUnicode_GET_LENGTH(p);
		str = PyBytes_AsString(PyUnicode_AsUTF8String(p));
		if (PyUnicode_IS_COMPACT_ASCII(p))
			printf("  type: compact ascii\n");
		else
			printf("  type: compact unicode object\n");
		printf("  length: %zd\n  value: %s\n", p_len, str);
	}
	else
	{
		printf("  [ERROR] Invalid String Object\n");
	}
	fflush(stdout);
}

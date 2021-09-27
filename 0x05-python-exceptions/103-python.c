#include "Python.h"
#include <stdio.h>
#include <float.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints information about Python list. Such as size, and
 * amount of memory allcoated. What type each element is and if it is a type
 * 'bytes' or 'float', print additional information on the element.
 *
 * @p: Pointer to a Python object.
 *
 * Return: void.
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t p_size;
	Py_ssize_t idx;
	PyObject *n;

	printf("[*] Python list info\n");
	if (PyList_Check(p))
	{
		p_size = ((PyVarObject *)(p))->ob_size;
		printf("[*] Size of the Python List = %zd\n", p_size);
		printf("[*] Allocated = %zd\n", ((PyListObject *) (p))->allocated);
		for (idx = 0; idx < p_size; idx++)
		{
			n = ((PyListObject *) (p))->ob_item[idx];
			printf("Element %zd: %s\n", idx, (n->ob_type)->tp_name);
			if (PyBytes_Check(n))
				print_python_bytes(n);
			else if (PyFloat_Check(n))
				print_python_float(n);
		}
	}
	else
	{
		printf("  [ERROR] Invalid List Object\n");
	}
	fflush(stdout);
}

/**
 * print_python_bytes - Checks if the object is a Python bytes object. If so
 * print the size, attempt to print it as a string and the first 10 bytes at
 * most in hexadecimal.
 *
 * @p: Pointer to a Python object.
 *
 * Return: void.
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t p_size;
	Py_ssize_t idx;
	Py_ssize_t max;
	char *str;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(p))
	{
		p_size = PyBytes_Size(p);
		str = ((PyBytesObject *) p)->ob_sval;
		printf("  size: %zd\n  trying string: %s\n", p_size, str);
		if (p_size < 10)
			max = p_size + 1;
		else
			max = 10;
		printf("  first %zd bytes: ", max);
		for (idx = 0; idx < max - 1; idx++)
			printf("%02x ",  (unsigned char) str[idx]);
		printf("%02x\n",  (unsigned char) str[max - 1]);
	}
	else
	{
		printf("  [ERROR] Invalid Bytes Object\n");
	}
	fflush(stdout);
}

/**
 * print_python_float - Checks if the object is a Python float object. If so
 * print the float value. If it is not, print an error message.
 *
 * @p: Pointer to a Python object.
 *
 * Return: void.
 */
void print_python_float(PyObject *p)
{
	PyObject *convert;

	printf("[.] float object info\n");
	if (PyFloat_Check(p))
	{
		convert = PyObject_Repr(p);
		convert = PyUnicode_AsEncodedString(convert, "utf-8", "~E~");
		printf("  value: %s\n", ((PyBytesObject *) convert)->ob_sval);
	}
	else
	{
		printf("  [ERROR] Invalid Float Object\n");
	}
	fflush(stdout);
}

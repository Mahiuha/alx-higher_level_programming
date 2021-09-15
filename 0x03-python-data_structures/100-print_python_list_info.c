#include <Python.h>
#include <stdio.h>
/**
 * print_python_list_info - print python
 * @p: input
 */
void print_python_list_info(PyObject *p)
{
	unsigned int l_idx;
	unsigned int len;
	unsigned int allocated;
	PyTypeObject *type;
	const char *name;

	if (p == NULL)
		return;

	len = (unsigned int) PyList_Size(p);
	allocated = (unsigned int) ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %d\n", len);
	printf("[*] Allocated = %d\n", allocated);

	for (l_idx = 0; l_idx < len; l_idx++)
	{
		type = PyList_GET_ITEM(p, l_idx)->ob_type;
		name = type->tp_name;
		printf("Element %d: %s\n", l_idx, name);
	}
}

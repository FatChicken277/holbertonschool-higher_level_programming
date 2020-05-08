#include <Python.h>
#include <object.h>
#include <bytesobject.h>
void print_python_bytes(PyObject *p);

/**
 * print_python_list - print info
 * @p: object
 */

void print_python_list(PyObject *p)
{

	long int len;
	int i;
	PyObject *item, *tuple;

	tuple = PyList_AsTuple(p);
	len = PyTuple_Size(tuple);
	PyListObject *aux = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %li\n", len);
	printf("[*] Allocated = %li\n", aux->allocated);

	for (i = 0; i < len; i++)
	{
		item = PyTuple_GetItem(tuple, i);
		if (PyFloat_Check(item))
			printf("Element %d: float\n", i);
		if (PyTuple_Check(item))
			printf("Element %d: tuple\n", i);
		if (PyList_Check(item))
			printf("Element %d: list\n", i);
		if (PyLong_Check(item))
			printf("Element %d: int\n", i);
		if (PyUnicode_Check(item))
			printf("Element %d: str\n", i);
	}
}

/**
 * print_python_bytes - print info
 * @p: object
 */


void print_python_bytes(PyObject *p)
{
	int size, i;
	PyBytesObject *aux = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	if (PyBytes_Check(p))
	{
		printf("  size: %ld\n", PyBytes_Size(p));
		printf("  trying string: %s\n", aux->ob_sval);

		if (((PyVarObject *)p)->ob_size > 10)
			size = 10;
		else
			size = ((PyVarObject *)p)->ob_size + 1;
		printf("  first %d bytes: ", size);
		for (i = 0; i < size; i++)
		{
			printf("%02hhx", aux->ob_sval[i]);
			if (i + 1 == size)
				printf("\n");
			else
				printf(" ");
		}
	}
	else
		printf("  [ERROR] Invalid Bytes Object\n");
}

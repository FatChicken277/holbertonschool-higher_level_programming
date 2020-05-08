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
	const char *type;
	len = ((PyVarObject *)p)->ob_size;
	PyListObject *aux = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %li\n", len);
	printf("[*] Allocated = %li\n", aux->allocated);

	for (i = 0; i < len; i++)
	{
		type = aux->ob_item[i]->ob_type->tp_name;
		printf("Element %d: %s\n", i, type);
		if (strcmp(type, "bytes") == 0)
			print_python_bytes(aux->ob_item[i]);
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

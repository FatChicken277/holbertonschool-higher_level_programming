#include <Python.h>
#include <object.h>
#include <bytesobject.h>
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

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

	fflush(stdout);
	printf("[*] Python list info\n");
	if (PyList_Check(p))
	{
		printf("[*] Size of the Python List = %li\n", len);
		printf("[*] Allocated = %li\n", aux->allocated);

		for (i = 0; i < len; i++)
		{
			type = aux->ob_item[i]->ob_type->tp_name;
			printf("Element %d: %s\n", i, type);
			if (strcmp(type, "bytes") == 0)
				print_python_bytes(aux->ob_item[i]);
			if (strcmp(type, "float") == 0)
				print_python_float(aux->ob_item[i]);
			fflush(stdout);
		}
	}
	else
	{
		printf("  [ERROR] Invalid List Object\n");
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

	fflush(stdout);
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
			fflush(stdout);
		}
	}
	else
		printf("  [ERROR] Invalid Bytes Object\n");
}

/**
 * print_python_float - print info
 * @p: object
 */
void print_python_float(PyObject *p)
{
	double faux;
	char *str;
	PyFloatObject *aux = (PyFloatObject *)p;

	fflush(stdout);
	printf("[.] float object info\n");
	if (PyFloat_Check(p))
	{
		faux = aux->ob_fval;
		str = PyOS_double_to_string(faux, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
		printf("  value: %s\n", str);
	}
	else
		printf("  [ERROR] Invalid Float Object\n");
}

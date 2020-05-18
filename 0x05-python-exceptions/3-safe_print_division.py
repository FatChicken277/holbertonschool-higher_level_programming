#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        exception = a / b
    except ZeroDivisionError:
        exception = None
    finally:
        print("Inside result: {}". format(exception))
        return exception

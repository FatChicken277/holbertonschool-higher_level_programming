#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        exception = a / b
        return exception
    except ZeroDivisionError:
        exception = None
        return exception
    finally:
        print("Inside result: {}". format(exception))

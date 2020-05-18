#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    a = None
    try:
        a = fct(*args)
    except Exception as error:
        print("Exception: {}".format(error), file=sys.stderr)
    return a

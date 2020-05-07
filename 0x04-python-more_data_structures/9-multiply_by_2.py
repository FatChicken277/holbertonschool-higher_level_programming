#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    a = {}
    for x, y in a_dictionary.items():
        a.update({x: y*2})
    return a

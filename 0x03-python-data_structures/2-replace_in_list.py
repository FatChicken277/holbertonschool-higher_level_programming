#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    i = len(my_list)
    if idx == i:
        i -= 1
    if idx > i or idx < 0:
        return my_list
    my_list[idx] = element
    return(my_list)

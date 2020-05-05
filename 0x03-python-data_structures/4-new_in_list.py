#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy = my_list.copy()
    i = len(copy)
    if idx == i:
        i -= 1
    if idx > i or idx < 0:
        return copy
    copy[idx] = element
    return(copy)

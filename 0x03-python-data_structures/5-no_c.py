#!/usr/bin/python3
def no_c(my_string):
    string = list(my_string)
    word = "cC"
    for i in word:
        C = string.count(i)
        while C != 0:
            C = string.index(i)
            del(string[C])
            C = string.count("c")
    return "".join(string)

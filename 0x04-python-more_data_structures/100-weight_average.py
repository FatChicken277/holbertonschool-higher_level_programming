#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        add, mul = 0, 0
        for x in my_list:
            mul = mul + (x[0] * x[1])
            add = add + x[1]
        return mul/add
    return 0

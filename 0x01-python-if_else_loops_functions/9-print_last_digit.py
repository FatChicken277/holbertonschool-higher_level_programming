#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        result = ((number % - 10) * -1)
    else:
        result = ((number % 10))
    print("{}".format(result), end="")
    return result

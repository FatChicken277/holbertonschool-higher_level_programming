#!/usr/bin/python3
for first_digit in range(10):
    for second_digit in range(10):
        if second_digit != first_digit:
            if first_digit < second_digit:
                print(first_digit, end="")
                if first_digit == 8 and second_digit == 9:
                    print(second_digit)
                else:
                    print(second_digit, end=", ")

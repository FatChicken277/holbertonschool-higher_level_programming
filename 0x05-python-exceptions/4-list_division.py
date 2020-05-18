#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            new_list.append(my_list_1[i] / my_list_2[i])
            message = ""
        except ZeroDivisionError:
            new_list.append(0)
            message = "division by 0"
        except TypeError:
            new_list.append(0)
            message = "wrong type"
        except IndexError:
            new_list.append(0)
            message = "out of range"
        finally:
            if message == "":
                print(message, end="")
            else:
                print(message)
    return new_list

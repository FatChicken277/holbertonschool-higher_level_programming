#!/usr/bin/python3
def roman_to_int(roman_string):
    dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    a = []
    if str != type(roman_string) or not roman_string:
        return None

    for i in roman_string:
        for j, v in dic.items():
            if i == j:
                a.append(v)
    p = a[:1]
    cur = a[0]
    for i in a[1:]:
        if i == cur:
            p[-1] += i
        else:
            p.append(i)
            cur = i
    if len(p) % 2 != 0:
        p.append(0)
    k = 0
    for x, y in zip(p, p[1:]):
        if k == 0:
            acum = p[0]
        if acum >= y:
            acum += y
            k = 1
        else:
            acum = y - x
            k = 1
    return acum

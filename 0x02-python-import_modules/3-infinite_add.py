#!/usr/bin/python3
def args(args):
    lenn = len(args) - 1
    result = 0
    if lenn != 0:
        for i in range(lenn):
            result += int(args[i+1])
    print("{0}".format(result))

if __name__ == "__main__":
    import sys
    args(sys.argv)

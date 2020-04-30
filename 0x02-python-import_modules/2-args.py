#!/usr/bin/python3
def args(args):
    lenn = len(args) - 1
    if lenn == 0:
        print("0 arguments.")
    elif lenn == 1:
        print("{0} argument:".format(lenn))
        print("{0}: {1}".format(lenn, args[lenn]))
    elif lenn > 1:
        print("{0} arguments:".format(lenn))
        for i in range(lenn):
            print("{0}: {1}".format(i+1, args[i+1]))

if __name__ == "__main__":
    import sys
    args(sys.argv)

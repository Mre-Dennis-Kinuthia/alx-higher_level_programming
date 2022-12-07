#!/usr/bin/python3
from sys import argv
def print_arg(argv):
    n = len(argv) - 1
    if n == 1:
        print("{:d} argument:".format(n))
    elif n == 0:
        print("{:d} argument.".format(n))
    else:
        print("{:d} arguments:".format(n))
        i = 1
        while i <= n:
            print("{:d}: {:s}".format(i, argv[i]))
            i += 1

if __name__ == "__main__":
    print_arg(argv)

#!/usr/bin/python3
import calculator_1.py
import sys

args_count = len(argv)
def my_calc():
    if args_count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")

        return 1
    elif argv[2] != '-' or argv[2] != '+' or argv[2] != '*' or argv[2] != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        return 1
    else:
        print("{:d} {:s} = {:d}".format(argv[1], argv[2], argv[3]))


if __name__ == "__main__":
    my_calc()

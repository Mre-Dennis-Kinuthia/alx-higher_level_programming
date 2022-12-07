#!/usr/bin/python3


def my_calc():
    args_count = len(sys.argv)
    if args_count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")

        return 1
    elif sys.argv[2] != '-' or sys.argv[2] != '+' or sys.argv[2] != '*' or sys.argv!= '/':
        print("Unknown operator. Available operators: +, -, * and /")
        return 1
    else:
        print("{:d} {:s} = {:d}".format(sys.argv[1], sys.argv[2], sys.argv[3]))


if __name__ == "__main__":
    #import calculator_1.py
    import sys
    my_calc()

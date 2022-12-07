#!/usr/bin/python3


def my_calc():
    args_count = len(sys.argv)
    if args_count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = sys.argv[1]
    operator = sys.argv[2]
    b = sys.argv[3]
    elif sys.argv[2] != '-' and sys.argv[2] != '+' and sys.argv[2] != '*' and sys.argv!= '/':
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    else:
        print("{:d} {:s} = {:d}".format(a, operator, b, add(a, b)))
        print("{:d} {:s} = {:d}".format(a, operator, b, sub(a, b)))
        print("{:d} {:s} = {:d}".format(a, operator, b, mul(a, b)))
        print("{:d} {:s} = {:d}".format(a, operator, b, div(a, b)))


if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys
    my_calc()

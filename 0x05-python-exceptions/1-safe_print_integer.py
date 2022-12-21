#!/usr/bin/python3

def safe_print_integer(value):
    try:
        if value is not None:
            print("{:d}".format(value))
            return True
        elif value is not str:
            print()
            return True
    except ValueError:
        return False

#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    if len(agrv) < 0:
        print("")
    else:
        for i in agrv:
            print("{:d}", " ", "{:s}".format(len(agrv), agrv[i]))
#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    j = chr(i)
    if j not in "qe":
        print("{:s}".format(chr(i)), end="")

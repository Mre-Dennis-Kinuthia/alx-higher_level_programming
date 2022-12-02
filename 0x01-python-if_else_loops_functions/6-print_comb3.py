#!/usr/bin/python3

for i in range (1, 90):
    if i != 89:
        print("{:02d}".format(i), end=", ")
    else:
        print("{:d}".format(i))

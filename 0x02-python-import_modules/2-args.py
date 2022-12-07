#!/usr/bin/python3
def
if __name__ == "__main__":
    from sys import argv
    count = len(argv)
    
    if count == 1:
        print("0 arguments.")
    elif count == 2:
        print("{:d} arguments:".format(count - 1))
    else:
        print("{:d}} arguments:".format(count - 1))
        
    for i in range(1, count):
        print("{:d}: {:s}".format((i), argv[i])

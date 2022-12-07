#!/usr/bin/python3
if __name__ == "__main__":
    from sys import agrv
    
    count = len(agrv)
    sum = 0
     
    for i in range(count):
        sum = count + sum
    print("{:d}".fomart(sum))
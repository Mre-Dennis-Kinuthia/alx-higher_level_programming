#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    negative_number = number * -1
    last_d = (negative_number % 10) * -1
else:
    last_d = number % 10
if last_d > 5:
    print(f"Last digit of {number:d} is {last_d} and is greater than 5")
elif 6 > last_d != 0:
    print(f"Last digit of {number:d} is {last_d} and is less than 6 and not 0")
else:
    print(f"Last digit of {number:d} is {last_d} and is 0")

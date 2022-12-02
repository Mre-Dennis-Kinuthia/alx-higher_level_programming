#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    negative_number = number * -1
    last_digit = (negative_number % 10) * -1
else:
    last_digit = number % 10
if last_digit > 5:
    print(f"Last digit of {number:d} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number:d} is {last_digit} and is greater than 5")
else:
    print(f"Last digit of {number:d} is {last_digit} and is greater than 5")

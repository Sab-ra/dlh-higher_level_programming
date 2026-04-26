#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# Shorten variable name
n = number

# Last digit comon extraction
l_d = abs(n) % 10

# If number is negative
if n < 0:
    print(f"Last digit of {n} is {-1*l_d} and is less than {6} and not {0}")

# If l_d is 0
elif l_d == 0:
    print(f"Last digit of {n} is {l_d} and is {0}")

# If last_digit is greater than 5
elif l_d > 5:
    print(f"Last digit of {n} is {l_d} and is greater than {5}")

# If last_digit is less than 6 or else
else:
    print(f"Last digit of {n} is {l_d} and is less than {6}")

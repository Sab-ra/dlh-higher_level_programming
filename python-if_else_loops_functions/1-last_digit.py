#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# Number to string and last_char
last_char = number(type(str))[-1]

# The char to int: last_digit
last_digit = last_char(type(int))

# If number is negative
if number < 0:
    print(f"Last digit of {number} is {-1*last_digit} and is less than {6} and not {0}")

# If last_digit is 0
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is {0}")

# If last_digit is greater than 5
elif last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than {5}")

# If last_digit is less than 6 or else
else:
    print(f"Last digit of {number} is {last_digit} and is less than {6}")

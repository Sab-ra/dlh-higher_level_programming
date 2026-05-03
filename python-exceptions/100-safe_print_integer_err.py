#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        if isinstance(value, bool):
            raise TypeError("an integer is required")
        print("{:d}".format(value))
        return True
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False

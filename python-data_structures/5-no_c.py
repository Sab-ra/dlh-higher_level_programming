#!/usr/bin/python3
def no_c(my_string):
    your_ctring = ""
    for c in my_string:
        if c != "c" or c != "C":
            your_string = my_string + c
    return your_string

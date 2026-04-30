#!/usr/bin/python3
def max_integer(my_list=[]):
    i = 0
    if len(my_list) == 0:
        return None
    else:
        a = my_list[0]
        while i < len(my_list):
            if a >= my_list[i]:
                i += 1
                continue
            else:
                a = my_list[i]
                i += 1
        return a

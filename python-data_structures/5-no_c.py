#!/usr/bin/python3
def no_c(my_string):
    char_list = list(my_string)
    new_string = ''
    for i in char_list:
        if i == 'c':
            continue
        elif i == 'C':
            continue
        else:
            new_string = new_string + i
        return new_string

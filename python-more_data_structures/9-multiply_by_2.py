#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    result = {}
    i = 0
    while i < len(a_dictionary):
        result[(list(a_dictionary)[i])] = a_dictionary[list(a_dictionary)[i] * 2]
        i += 1
    return result

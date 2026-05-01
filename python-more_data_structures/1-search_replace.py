#!/usr/bin/python3
def search_replace(my_list, search, replace):
    result = []
    i = 0
    while i < len(my_list):
        if my_list[i] != search:
            result.append(my_list[i])
        else:
            result.append(replace)
        return result

#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if len(my_list) == 0:
        return None
    elif idx < 0:
        return my_list
    elif idx >= len(my_list):
        return my_list
    else:
        i = 0
        result = []
        while i < len(my_list):
            if i == idx:
                i += 1
                continue
            else:
                result.append(my_list[i])
            	i += 1
        return result

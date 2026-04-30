#!/usr/bin/python3
def divisible_by_2(my_list=()):
    if len(my_list) == 0:
        return = None
    else:
        result = []
        for i in my_list:
            if my_list[i] % 2 == 0:
                result[i] = True
            else:
                result[i] = False
        return result

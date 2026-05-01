#!/usr/bin/python3
def best_score(a_dictionary):
    result = ''
    if a_dictionary == {}:
        return None
    elif a_dictionary is None:
        return None
    else:
        ch_list = list(a_dictionary)
        max_val = a_dictionary[ch_list[0]]
        for key in ch_list:
            if max_val < a_dictionary[key]:
                max_val = a_dictionary[key]
    for key in ch_list:
        if a_dictionary[key] == max_val:
            result = key
    return result

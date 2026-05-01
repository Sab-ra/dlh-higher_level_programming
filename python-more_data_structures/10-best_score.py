#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == {}:
        return None
    else:
        ch_list = list(a_dictionary)
        max_val = a_dictionary[ch_list[0]]
        for key in ch_list:
             if max_val < a_dictionary[key]:
                 max_val = a_dictionary[key]
    return max_val
             

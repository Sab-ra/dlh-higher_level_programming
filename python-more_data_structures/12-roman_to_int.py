#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_weights = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    if type(roman_string) is not str:
        return 0
    elif type(roman_string) is None:
        return 0
    else:
        roman_string = roman_string.upper()
        arab_list = []
        for c in roman_string:
            arab_list.append(roman_weights[c])
    num_list = []
    for i in arab_list:
        num_list.append(arab_list[0])
        if i > 0:
             if arab_list[i] > arab_list[i - 1]:
                 if arab_list[i] == 1000:
                     del num_list[-1]
                     num_list[-1] = 900
                 if arab_list[i] == 500:
                     del num_list[-1]
                     num_list[-1] = 400
                 if arab_list[i] == 100:
                     del num_list[-1]
                     num_list[-1] = 90
                 if arab_list[i] == 50:
                     del num_list[-1]
                     num_list[-1] = 40
                 if arab_list[i] == 10:
                     del num_list[-1]
                     numb_list[-1] = 9
                 if arab_list[i] == 5:
                     del num_list[-1]
                     numb_list[-1] = 4

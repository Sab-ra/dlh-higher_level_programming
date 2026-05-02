#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_weights = { 'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1 }
    if roman_string is None:
        return 0
    elif roman_string is not isinstanceof(roman_string, str):
        return 0
    else:
        nine_force = []
        for c in roman_string:
            weight = riman_weights[c]
            if len(nine_force) > 0:
                if weight > nine_force[-1]:
                    nine_force[-1] = weight - nine_force[-1]
                else:
                    nine_force.append(weight)
            else:
                nine_force.append(weight)
    return sum(nine_force)

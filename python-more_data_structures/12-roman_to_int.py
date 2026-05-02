#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = ['M', 'D', 'C', 'L', 'X', 'V', 'I']
    weights = [1000, 500, 100, 50, 10, 5, 1]
    roman_weights = dict(zip(roman, weights))
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    else:
        nine_force = []
        for c in roman_string:
            weight = roman_weights[c]
            if len(nine_force) > 0:
                if weight > nine_force[-1]:
                    nine_force[-1] = weight - nine_force[-1]
                else:
                    nine_force.append(weight)
            else:
                nine_force.append(weight)
        result = sum(nine_force)
        return result

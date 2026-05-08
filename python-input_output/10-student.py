#!/usr/bin/python3
"""Class student ready to DB"""


class Student:
    """Student that goes to DB"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list):
            new_dict = {}
            for key in attrs:
                if attrs[key] != None:
                    new_dict[key] = getattr(self, key)
                    return new_dict
                else:
                    return self.__dict__

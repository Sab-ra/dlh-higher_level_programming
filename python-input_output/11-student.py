#!/usr/bin/python3
"""Class student ready to DB"""


class Student:
    """Student that goes to DB"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation for JSON serialization"""
        if attrs is None:
            return self.__dict__

        if isinstance(attrs, list):
            new_dict = {}
            for key in attrs:
                if hasattr(self, key):
                    new_dict[key] = getattr(self, key)
            return new_dict
        
    def reload_from_json(self, json):
        """Rewrites Class attributes"""

        self.__dict__.update(json)

#!/usr/bin/python3
"""Serialize with pickle"""


import pickle


class CustomObject:
    """Custom class that supports pickle ser-tion."""

    def __init__(self, name, age, is_student):
        """Initialize object"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))


    def serialize(self, filename):
        """Self to pickle file"""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (OSError, pickle.PicklingError):
            return None

    @classmethod
    def deserizlize(cls, filename):
        """Become unknown object"""
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
            return obj if isinstance(obj, cls) else None
        except (FileNotFoundError, OSError, EOFError, pickle.UnpicklingError):
            return None

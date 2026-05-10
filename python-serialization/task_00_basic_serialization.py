#!/usr/bin/python3
"""Module to serialize and deserialize"""


import json


def serialize_and_save_to_file(data, filename):
    """Data to file"""
    with open(filename, "w") as f:
        json.dump(data, f)
    print("Data serialized and saved to {}.".format(filename))

def load_and_deserialize(filename):
    """Data from file"""
    with open(filename) as f:
        try:
            json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

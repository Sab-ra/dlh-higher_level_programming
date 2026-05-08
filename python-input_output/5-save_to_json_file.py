#!/usr/bin/python3
"""Sends an object to a json file"""


import json


def save_to_json_file(my_obj, filename):
    """Will brake on pics"""
    with open(filename, mode="w", encoding="utf-8"):
        return filename.write(json.dumps(my_obj))

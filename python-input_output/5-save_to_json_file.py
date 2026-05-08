#!/usr/bin/python3
"""Sends an object to a json file"""


import json


def save_to_json_file(my_obj, filename):
    """Under filename you need a file object"""
    with open(filename, mode="w", encoding="utf-8") as file_object:
        return json.dump(my_obj, file_object)

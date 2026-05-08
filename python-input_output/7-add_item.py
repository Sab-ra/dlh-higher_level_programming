#!/usr/bin/python3
"""Module handles arguments from CL and File"""


import sys


load = __import__('6-load_from_json_file').load_from_json_file
save = __import__('5-save_to_json_file').save_to_json_file


def add_item(file="add_item.json"):
    """Add sys args to file args"""
    try:
        thing = load(file)
    except FileNotFoundError:
        thing = []
    another_thing = []
    for i in range(1, len(sys.argv)):
        another_thing.append(sys.argv[i])
    thing += another_thing
    return save(thing, file)


add_item()

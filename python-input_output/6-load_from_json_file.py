#!/usr/bin/python3
"""How do you suck an obj out of JSON?"""


import json


def load_from_json_file(filename):
    """Use the stateless function"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

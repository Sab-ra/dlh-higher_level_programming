#!/usr/bin/python3
"""The essence of append"""


load = __import__('6-load_from_json_file').load_from_json_file
save = __import__('5-save_to_json_file').save_to_json_file

def add_item(sourse_file, output_file="add_item.json"):
    thing = load(sourse_file)
    return save(thing, output_file)

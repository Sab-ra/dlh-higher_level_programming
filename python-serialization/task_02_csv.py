#!/usr/bin/python3
"""CSV to JSON convenrsion module"""


import csv
import json


def convert_csv_to_json(filename):
    """CSV content to data.json"""
    try:
        with open(filename, "r", newline="") as csv_f:
            reader = csv.DictReader(csv_f)
            data = [row for row in reader]

        with open("data.json", "w") as json_f:
            json.dump(data, json_f)

        return True
    except (FileNotFoundError, OSError):
        return False

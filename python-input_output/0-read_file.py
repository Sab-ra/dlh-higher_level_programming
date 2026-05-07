#!/usr/bin/python3
"""Bery-bery dandjurious module"""


def read_file(filename=""):
    """If file bit enough--your comp will dye"""
    with open(filename, mode="r", encoding="utf-8") as file_to_read:
        print(file_to_read.read(), end="")

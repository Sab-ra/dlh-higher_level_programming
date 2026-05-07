#!/usr/bin/python3
"""Net dandjourious method"""


def write_file(filename="", text=""):
    """Filename may be relative or absolute"""
    with open(filename, mode="w", encoding="utf-8") as blank_page:
        blank_page.write(text)

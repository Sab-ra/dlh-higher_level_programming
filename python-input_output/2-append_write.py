#!/usr/bin/python3
"""Now you saving words!"""


def append_write(filename="", text=""):
    """You append, not destroy"""
    with open(filename, mode="a", encoding="utf-8") as page_to_write:
        s = str(text)
        return page_to_write.write(s)

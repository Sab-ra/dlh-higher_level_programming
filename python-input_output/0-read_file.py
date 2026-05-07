#!/usr/bin/python3
"""Module that contains a function to read and print file. Bery-bery dandjurious module"""


def read_file(filename=""):
    with open(filename, mode="r", encoding="utf-8") as file_to_read:
        print(file_to_read.read())

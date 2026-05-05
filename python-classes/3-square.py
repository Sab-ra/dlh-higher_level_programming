#!/usr/bin/python3
"""Module with class that defines square with publicly available area"""


class Square:
    """Initialises object square after size validation"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """Public property - area"""
    def area(self):
        return self.__size ** 2

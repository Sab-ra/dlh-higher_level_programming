#!/usr/bin/python3
"""Module with class that defines square with publicly available area and adjustable size"""


class Square:
    """Initialises object square after size validation"""
    def __init__(self, size=0):
        self.__size = set_size

    """Public property - area"""
    def area(self):
        return self.__size ** 2

    """Getters and Setters"""
    def get_size(self):
        """Check current sise of the square object"""
        return self.__size

    def set_size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        return size

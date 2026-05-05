#!/usr/bin/python3
"""Module with class that defines square with publicly available area and adjustable size"""


class Square:
    """Initialises object square after size validation"""
    def __init__(self, size=0):
        """Initialize a square with size validation.
        Args:
            size: The size of the square (must be an integer >= 0).
        """
        self.set_size(__size)

    def area(self):
        """Return current square area"""
        return self.__size ** 2

    """Getters and Setters"""

    def get_size(self):
        """Check current sise of the square object"""
        return self.__size

    def set_size(self, size):
        """Single sourse of truth to set private property size of the square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = size

#!/usr/bin/python3
"""
Module Rectangle
"""


class Rectangle:
    """Rectangle is made of more than one triangles"""

    def __init__(self, width=0, height=0):
        """Initialize rectangle with """

        self.width = width
        """Attr: horizontal measure of the rectangle"""

        self.height = height
        """Attr: vertical measure of the rectangle"""

    def area(self):
        """Returns rectangle area"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns rectangle perimeter"""
        return 2 ** (self.__width + self.__height)

    """Getters & Setters"""

    @property
    def width(self):
        """Retrieve private attr __width"""

        return self.__width

    @width.setter
    def width(self, value):
        """Validate & set private instance attr: __width"""

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """doc"""
        return self.__height

    @height.setter
    def height(self, value):
        """Validate & set private instance attr: __height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

#!/usr/bin/python3
"""Module with class that defines square with publicly available area and adjustable size"""


class Square:
    """Initialises object square after size validation"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a square through the setter."""
        self.size = size
        self.position = position

    def area(self):
        """Return current square area"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square"""
        if self.__size > 0:
            x = self.__size
            blank = self.__position[0]
            for i in range(x):
                print((" " * blank) + ("#" * x))
        else:
            print()


    """Getters and Setters"""

    @property
    def size(self):
        """Check current sise of the square object"""
        return self.__size

    @size.setter
    def size(self, value):
        """Single sourse of truth to set private property size of the square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Check qurrent position coordinates"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets position on birth of an instance, or during it's life"""
        desired_outcome = [True, True, True]
        outcome = []
        if len(value) == 2:
            outcome.append(True)
        else:
            outcome.append(False)
        if isinstance(value, tuple):
            outcome.append(True)
        else:
            outcome.append(False)
        if value[0] >= 0 and value[1] >= 0:
            outcome.append(True)
        else:
            outcome.append(False)

        if desired_outcome != outcome:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
            

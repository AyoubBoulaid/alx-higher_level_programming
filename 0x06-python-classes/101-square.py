#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Define a square with size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.

        Args:
            size (int): The size of the square.
            position (int, int): The position of the square.
        """
        self._size = size
        self._position = position

    @property
    def size(self):
        """Get or set the current size of the square."""
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be greater than or equale to 0")
        self._size = value

    @property
    def position(self):
        """Get or set the position of the square."""
        return (self._position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(num, int) for num in value) or not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        """calculate the area of the square."""
        return self._size ** 2

    def my_print(self):
        """Print the square with the # character."""
        if self._size == 0:
            print("")
            return

        [print("") for i in range(0, self._position[1])]
        for i in range(0, self._size):
            [print(" ", end="") for j in range(0, self._position[0])]
            [print("#", end="") for k in range(0, self._size)]
            print("")

    def __str__(self):
        """Define the print() representation of a Square."""
        if self._size != 0:
            [print("") for i in range(0, self._position[1])]
        for i in range(0, self._size):
            [print(" ", end="") for j in range(0, self._position[0])]
            [print("#", end="") for k in range(0, self._size)]
            if i != self._size - 1:
                print("")
        return ("")

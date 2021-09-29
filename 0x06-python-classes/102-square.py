
#!/usr/bin/python3
"""Module containing the Square class"""


class Square:
    """The Square class"""
    def __init__(self, size=0):
        """Initializing an instance of Square
        Args:
            size (int): The size of the Square instance. Default value is 0.
        """
        self.size = size

    @property
    def size(self):
        """int: size of the Square instance"""
        return self.__size

    @size.setter
    def size(self, size):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Returns the current square area of the instance
        Returns:
            int: The square of size
        """
        return self.__size ** 2

    def __eq__(self, other):
        """Check if the area of the instance is the same as the area of 'other'.
        Returns:
            bool: The return Value. True if self.area == other.area. False
                otherwise, or 'other' is not of type Square.
        """
        if isinstance(other, Square):
            if self.area() == other.area():
                return True
            else:
                return False
        else:
            return False

    def __ne__(self, other):
        """Check if the area of the instance is not the same as the area of
            'other'.
        Returns:
            bool: The return Value. True if self.area != other.area. False
                otherwise, or 'other' is not of type Square.
        """
        if isinstance(other, Square):
            if self.area() != other.area():
                return True
            else:
                return False
        else:
            return False

    def __gt__(self, other):
        """Check if the area of the instance is greater than the area of 'other'.
        Returns:
            bool: The return Value. True if self.area > other.area. False
                otherwise, or 'other' is not of type Square.
        """
        if isinstance(other, Square):
            if self.area() > other.area():
                return True
            else:
                return False
        else:
            return False

    def __ge__(self, other):
        """Check if the area of the instance is greater than or equal to the
            area of 'other'.
        Returns:
            bool: The return Value. True if self.area >= other.area. False
                otherwise, or 'other' is not of type Square.
        """
        if isinstance(other, Square):
            if self.area() >= other.area():
                return True
            else:
                return False
        else:
            return False

    def __lt__(self, other):
        """Check if the area of the instance is less than the area of 'other'.
        Returns:
            bool: The return Value. True if self.area < other.area. False
                otherwise, or 'other' is not of type Square.
        """
        if isinstance(other, Square):
            if self.area() < other.area():
                return True
            else:
                return False
        else:
            return False

    def __le__(self, other):
        """Check if the area of the instance is less than or equal to the area
            of 'other'.
        Returns:
            bool: The return Value. True if self.area <= other.area. False
                otherwise, or 'other' is not of type Square.
        """
        if isinstance(other, Square):
            if self.area() <= other.area():
                return True
            else:
                return False
        else:
            return False

#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size, color="Unknown"):
        self.brand = brand
        self.size = size
        self.color = color
        self.condition = "Used"  # Default condition

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, brand):
        if isinstance(brand, str) and brand:
            self._brand = brand
        else:
            print("Brand must be a non-empty string.")

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if isinstance(size, (int, float)) and size > 0:
            self._size = size
        else:
            print("size must be an integer")

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        if isinstance(color, str) and color:
            self._color = color
        else:
            print("Color must be a non-empty string.")

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"

#!/usr/bin/python3
"""Modules fo Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    '''A Square class'''

    def __init__(self, size, x=0, y=0, id=None):
        """constructre"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}".format(self.id,
                                                  self.x,
                                                  self.y,
                                                  self.size))

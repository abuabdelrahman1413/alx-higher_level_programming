#!/usr/bin/python3
"""return class __dict__"""


class Student:
    """class student"""

    def __init__(self, first_name, last_name, age):
        """init"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return dictionary representation of a Student instance"""
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
        }

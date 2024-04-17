#!/usr/bin/python3
"""Module to convert json to opject"""
import json


def from_json_string(my_str):
    """Function to convert json to object"""
    return json.loads(my_str)

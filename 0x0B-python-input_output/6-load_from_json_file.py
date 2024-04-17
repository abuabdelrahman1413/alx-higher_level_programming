#!/usr/bin/python3
"""Module to create an object from json file"""
import json


def load_from_json_file(filename):
    """Function return object from json file"""
    with open(filename, "r") as f:
        json_object = json.load(f)
    return json_object

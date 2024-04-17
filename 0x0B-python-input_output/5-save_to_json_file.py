#!/usr/bin/python3
"""Module write json to file"""
import json


def save_to_json_file(my_obj, filename):
    """Write json to file"""
    with open(filename, "w") as outfile:
        # Convert the object to a JSON string using json.dumps
        json_string = json.dumps(my_obj)
        # Write the JSON string to the file
        outfile.write(json_string)

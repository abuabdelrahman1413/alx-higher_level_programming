#!/usr/bin/python3
"""Module script add args to json"""

import sys

from 6-load_form_json_file import load_from_json_file

from 5-save_to_json_file import save_to_json_file

if __name__ == "__main__":
    try:
        lst = load_from_json_file("add_item.json")
    except FileNotFoundError():
        lst = []
    lst.extend(sys.argv[1:])
    save_to_json_file(lst, "add_item.json")

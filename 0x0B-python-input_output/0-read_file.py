#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints its contents to stdout.

    Args:
      filename: The path to the text file.
    """

    with open(filename, encoding="utf-8") as f:
        # Read all lines at once and print them
        contents = f.read()
        print(contents, end="")


# Example usage
read_file("/home/mohammed/Projects/alx-higher_level_programming/0x0B-python-input_output/my_file.txt")

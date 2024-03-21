#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    b_dictionary = a_dictionary.copy()
    for key, value in b_dictionary.items():
        value = value * 2
    return b_dictionary

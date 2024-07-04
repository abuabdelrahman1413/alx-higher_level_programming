#!/usr/bin/python3
"""peek of unsorted array O(1)"""
def find_peak(list_of_integers):
    """returns peak of unsorted array many peeks"""
    if list_of_integers:
        return max(list_of_integers)

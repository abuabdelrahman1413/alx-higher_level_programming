#!/usr/bin/python3
"""peek of unsorted array O(1)"""


def find_peak(list_of_integers):
    """returns peak of unsorted array many peeks"""
    if not list_of_integers:
        return None
    if len(list_of_integers) == 1:
        return 0
    if list_of_integers[0] > list_of_integers[1]:
        return 0
    if list_of_integers[-1] > list_of_integers[-2]:
        return len(list_of_integers) - 1
    low = 1
    high = len(list_of_integers) - 2

    while low <= high:
        mid = (low + high) // 2
        if (
            list_of_integers[mid] > list_of_integers[mid - 1]
            and list_of_integers[mid] > list_of_integers[mid + 1]
        ):
            return mid
        if list_of_integers[mid - 1] > list_of_integers[mid]:
            high = mid - 1
        else:
            low = mid + 1

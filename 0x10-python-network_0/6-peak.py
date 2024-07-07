#!/usr/bin/python3
"""peek of unsorted array O(1)"""


def find_peak(list_of_integers):
    """returns peak of unsorted array many peeks"""
    # if list is empty, return None

    if not list_of_integers or len(list_of_integers) == 0:
        return None

    # if list is only one element, return that element
    # if list has two elements, return the greater one
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    elif len(list_of_integers) == 2:
        return max(list_of_integers[0], list_of_integers[1])
    # if first and last elements are greater, return that
    if list_of_integers[0] > list_of_integers[1]:
        return list_of_integers[0]
    elif list_of_integers[-1] > list_of_integers[-2]:
        return list_of_integers[-1]
    else:
        i = 1
        while i < len(list_of_integers) - 1:
            if (
                list_of_integers[i] > list_of_integers[i - 1]
                and list_of_integers[i + 1] > list_of_integers[i]
            ):
                return list_of_integers[i]
            else:
                i += 1

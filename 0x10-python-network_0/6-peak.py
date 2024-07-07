# #!/usr/bin/python3
# """peek of unsorted array O(1)"""


# def find_peak(list_of_integers):
#     """returns peak of unsorted array many peeks"""
#     # if list is empty, return None

#     if not list_of_integers or len(list_of_integers) == 0:
#         return None

#     # if list is only one element, return that element
#     # if list has two elements, return the greater one
#     if len(list_of_integers) == 1:
#         return list_of_integers[0]
#     elif len(list_of_integers) == 2:
#         return max(list_of_integers[0], list_of_integers[1])
#     # if first and last elements are greater, return that
#     if list_of_integers[0] > list_of_integers[1]:
#         return list_of_integers[0]
#     elif list_of_integers[-1] > list_of_integers[-2]:
#         return list_of_integers[-1]
#     else:
#         i = 1
#         while i < len(list_of_integers) - 1:
#             if (
#                 list_of_integers[i] > list_of_integers[i - 1]
#                 and list_of_integers[i + 1] > list_of_integers[i]
#             ):
#                 return list_of_integers[i]
#             else:
#                 i += 1


#!/usr/bin/python3
"""This module defines the function `find_peak`
"""


def find_peak(list_of_integers):
    """This function finds a peak in a list of unsorted integers.
    Args:
        list_of_integers (list): list of the unsorted integers.
    Returns:
        the peak integer of the list.
    """
    li = list_of_integers
    if li == [] or li is None:
        return None
    if len(li) == 1:
        return li[0]
    elif len(li) == 2:
        return li[0] if li[0] > li[1] else li[1]
    # half = len(li) // 2
    # if (li[half] >= li[half - 1] and li[half] >= li[half + 1]):
    #     return li[half]

    # elif (li[half] < li[half - 1]):
    #     return find_peak(li[:half])
    # else:
    #     return find_peak(li[half+1:])
    if li[0] > li[1]:
        return li[0]
    elif li[len(li) - 1] > li[len(li) - 2]:
        return li[len(li) - 1]
    else:
        i = 1
        while i < (len(li) - 1):
            if li[i] > li[i - 1] and li[i] > li[i + 1]:
                return li[i]
            else:
                i += 1

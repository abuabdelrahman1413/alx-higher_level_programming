#!/usr/bin/python3
def best_score(a_dictionary):
    values = list(a_dictionary.values())
    max = values[0]
    for i in values:
        if max < i:
            max = i
    idx = values.index(max)
    keys = list(a_dictionary.keys())
    max_key = keys[idx]
    return max_key

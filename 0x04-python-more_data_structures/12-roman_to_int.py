#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    else:
        roman = {"I": 1, "V": 5, "X": 10,
                 "L": 50, "C": 100, "D": 500, "M": 1000}

        res = 0
        for i in range(len(roman_string)):
            if (
                i + 1 < len(roman_string)
                and roman[roman_string[i]] < roman[roman_string[i + 1]]
            ):
                res -= roman[roman_string[i]]
            else:
                res += roman[roman_string[i]]
    return res

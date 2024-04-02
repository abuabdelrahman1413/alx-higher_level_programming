#!/usr/bin/python3
import re


def safe_print_division(a, b):
    result = 0
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        result = None
        return None
    finally:
        print("Inside result: {}".format(result))

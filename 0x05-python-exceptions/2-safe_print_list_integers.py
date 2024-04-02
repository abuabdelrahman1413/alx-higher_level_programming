#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            try:
                print("{:d}".format(my_list[i]), end="")
                count += 1
            except (ValueError, TypeError):
                pass  # Silently skip non-integer elements
    except IndexError:
        pass  # Handle potential IndexError gracefully

    print()  # Add a newline after printing integers
    return count

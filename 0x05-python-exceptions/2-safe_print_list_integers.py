def safe_print_list_integers(my_list=[], x=0):
    """Prints the first x integers from a list, handling potential errors.

    Args:
        my_list: The list to print integers from.
        x: The number of elements to print.

    Returns:
        The number of integers printed.
    """

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

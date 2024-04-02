#!/usr/bin/python3
def safe_print_integer(value):
  """
  Prints the value if it's an integer, otherwise prints a message.

  Args:
      value: The value to check and print.
  """
  try:
    # Attempt to convert the value to an integer using type conversion
    int_value = int(value)
    print("{:d}".format())
    return True
  except ValueError:
    # If conversion fails (ValueError), print a message indicating non-integer
    return False

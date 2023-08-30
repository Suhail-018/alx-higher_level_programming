#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b  # Perform the division
    except ZeroDivisionError:
        result = None  # Handle division by zero
    finally:
        print("Inside result: {}".format(result))  # Print the result inside finally
        return result  # Return the result of the division

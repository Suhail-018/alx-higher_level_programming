#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed = 0  # Initialize a counter to keep track of printed integers

    try:
        for i in range(x):
            if my_list[i]:
                if isinstance(my_list[i], int):
                    print("{:d}".format(my_list[i]), end='')  # Print integers only
                    printed += 1
            else:
                raise IndexError
    except (IndexError, TypeError):
        return 1  # H and TypeError (non-integer)

    print()  # Print a newline after printing the integers
    return printed  # Return the number of integers actually printed

#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printed = 0  # Initialize a counter to keep track of printed elements

    try:
        for i in range(x):
            print(my_list[i], end='')  # Print the element without a newline
            printed += 1
    except IndexError:
        pass  # Handle IndexError by catching the exception

    print()  # Print a newline after printing the elements
    return printed  # Return the number of elements actually printed

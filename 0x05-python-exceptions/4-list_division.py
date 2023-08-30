#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []

    for i in range(list_length):
        try:
            dividend = my_list_1[i]
            divisor = my_list_2[i]
            if not isinstance(dividend, (int, float)) or not isinstance(divisor, (int, float)):
                raise TypeError("wrong type")  # Raise TypeError for non-integer or non-float
            result.append(dividend / divisor)
        except ZeroDivisionError:
            result.append(0)  # Division by zero
        except IndexError:
            print("out of range")  # List is too short
            result.append(0)  # Append 0 to the result list for out-of-range elements
        except Exception:
            print("division by 0")  # Catch all other exceptions

    return result

#!/usr/bin/python3

def uniq_add(my_list=[]):
    unique_sum = 0
    seen = set()  # To keep track of unique integers
    
    for num in my_list:
        if num not in seen:
            unique_sum += num
            seen.add(num)
    
    return unique_sum

# Test the function
my_list = [1, 2, 3, 1, 4, 2, 5]
result = uniq_add(my_list)
print("Result: {:d}".format(result))

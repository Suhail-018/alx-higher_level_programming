#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_sum = 0
    seen = set()
    for num in my_list:
        if num not in seen:
            unique_sum += num
            seen.add(num)
    return unique_sum

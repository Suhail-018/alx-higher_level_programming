#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
ls_dt = abs(number) % 10  # Get the last digit's absolute value
if number < 0:
    ls_dt = -ls_dt
if ls_dt > 5:
    print(f"Last digit of {number} is {ls_dt} and is greater than 5")
elif ls_dt == 0:
    print(f"Last digit of {number} is {ls_dt} and is 0")
else:
    print(f"Last digit of {number} is {ls_dt} and is less than 6 and not 0")

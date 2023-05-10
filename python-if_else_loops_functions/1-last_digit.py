#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last = number % -10
    out = f"The last digit of {number} is {last}"
elif number > 0:
    last = number % 10
    out = f"The last digit of {number} is {number % 10}"

if last == 0:
    out += " and is 0"
elif last > 5:
    out += " and is greater than 5"
elif last < 6:
    out += " and is less than 6 and not 0"
print(out)

#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

# Verify if the number is positive and get the last digit
if number >= 0:
    lastdigit = number % 10
# If the number is negative we multiply by a negative to have a positive number
else:
    lastdigit = number % (-10)

if lastdigit > 5:
    print("Last digit of {} is {:d} and is greater than 5"
          .format(number, lastdigit))

if lastdigit == 0:
    print("Last digit of {} is {:d} and is 0".format(number, lastdigit))

elif lastdigit < 6 != 0:
    print("Last digit of {} is {:d} and is less than 6 and not 0"
          .format(number, lastdigit))

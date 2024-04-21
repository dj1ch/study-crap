"""
Pasted from https://wiki.c2.com/?FizzBuzzTest=

The "Fizz-Buzz test" is an interview question designed to help filter out the 99.5% of programming job candidates who can't seem to program their way out of a wet paper bag. The text of the programming assignment is as follows:
"Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”."
"""

import time

# print up to 100, simple
for i in range(1,101):
    # mistake: dont use /, use % instead and check if the remainder is 0
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    # mistake: remember else block so int is not always printed
    else:
        print(i)
    # mistake: if this is a for loop we shouldn't be doing a += operation
    time.sleep(0.1)

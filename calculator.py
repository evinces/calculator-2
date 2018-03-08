"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

# from arithmetic import *
from arithmetic2 import *


def my_reduce(function, iterable):
    result = iterable[0]
    for i in range(1, len(iterable)):
        result = function(result, iterable[i])
    return result

# Your code goes here
while True:
    user_input = raw_input("> ")
    if user_input[0] == "q":
        break
    else:
        tokens = user_input.split(" ")
        try:
            for i in range(1, len(tokens)):
                tokens[i] = float(tokens[i])

        except ValueError:
            print "Please enter an operator followed by numbers."
            continue

        try:
            if tokens[0] == "+":
                print my_reduce(lambda x, y: add(x, y), tokens[1:])

            elif tokens[0] == "-":
                print reduce(lambda x, y: subtract(x, y), tokens[1:])

            elif tokens[0] == "*":
                print reduce(lambda x, y: multiply(x, y), tokens[1:])

            elif tokens[0] == "/":
                print reduce(lambda x, y: divide(x, y), tokens[1:])

            elif tokens[0] == "square":
                print square(tokens[1])

            elif tokens[0] == "cube":
                print cube(tokens[1])

            elif tokens[0] == "pow":
                print reduce(lambda x, y: power(x, y), tokens[1:])

            elif tokens[0] == "mod":
                print reduce(lambda x, y: mod(x, y), tokens[1:])

            else:
                print "Invalid command: Please try again."

        except IndexError:
            print "Invalid number of arguments."

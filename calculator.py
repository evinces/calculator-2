"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *
# from arithmetic2 import *


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
                print add(tokens[1:])

            elif tokens[0] == "-":
                print subtract(tokens[1:])

            elif tokens[0] == "*":
                print multiply(tokens[1:])

            elif tokens[0] == "/":
                print divide(tokens[1:])

            elif tokens[0] == "square":
                print square(tokens[1])

            elif tokens[0] == "cube":
                print cube(tokens[1])

            elif tokens[0] == "pow":
                print power(tokens[1], tokens[2])

            elif tokens[0] == "mod":
                print mod(tokens[1], tokens[2])

            else:
                print "Invalid command: Please try again."

        except IndexError:
            print "Invalid number of arguments."

"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic_new import *

while True:
    user_input = raw_input(">")
    user_input = user_input.split(" ")
    operator = user_input[0]
    user_lst = user_input[1:]
    number_lst = []

    for i in user_lst:
        if i.isdigit():
            number_lst.append(int(i))
        else:
            print "That is not a valid set of inputs."
            break

    print number_lst

    if operator == "square":
        print square(number_lst)

    elif operator == "cube":
        print cube(number_lst)

    elif operator == "+":
        print add(number_lst)

    elif operator == "-":
        print subtract(number_lst)

    elif operator == "*":
        print multiply(number_lst)

    elif operator == "pow":
        print power(number_lst)

    elif operator == "mod":
        print mod(number_lst)

    elif operator == "cubes+":
        print add_cubes(number_lst)

    elif operator == "x+":
        print add_mult(number_lst)

    elif operator.upper() == "Q" or operator.upper() == "QUIT":
        break

    else:
        print "That's not a valid option, please choose again"

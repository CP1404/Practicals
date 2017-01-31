"""
CP1404/CP5632 Practical
Recursion
"""


def do_it(n):
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)

# TODO: 1. write down what you think the output of this will be,
# TODO: 2. use the debugger to step through and see what's actually happening
print(do_it(5))


def do_something(n):
    if n < 0:
        print(n ** 2)
    do_something(n - 1)

# TODO: 3. write down what you think the output of this will be,
# TODO: 4. use the debugger to step through and see what's actually happening
# do_something(4)

# TODO: 5. fix the do_something() function so that it works the way it is probably supposed to :)

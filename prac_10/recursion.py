"""
CP1404/CP5632 Practical - Suggested Solution
Recursion
"""


def do_it(n):
    """Do... it."""
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)


# print(do_it(5))


def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    # if we get to zero, we're done... just return
    if n < 0:
        return
    # if we have not hit the base case (no else needed)
    # print the square of n, then do the same for n-1
    print(n ** 2)
    do_something(n - 1)


do_something(4)


def calculate_blocks(rows):
    """Calculate blocks needed for a given number of rows of a 2D pyramid."""
    # base case: we need zero blocks for zero (or fewer!) rows
    if rows <= 0:
        return 0
    # recursive case: each row contains the number of blocks as its row number
    # ... plus the rest of it
    return rows + calculate_blocks(rows - 1)


def build_pyramid():
    """Get user's pyramid size in rows and output the blocks needed."""
    # chosen_rows = 6
    chosen_rows = int(input("How many rows is your pyramid: "))
    print("For {} rows, you need {} blocks".format(chosen_rows,
                                                   calculate_blocks(
                                                       chosen_rows)))


build_pyramid()

"""
CP1404/CP5632 Practical
Recursion
"""
import doctest


def do_it(n):
    """Do... it.
    Recursively calculate the sum of n % 2 for numbers from n down to 1.
    """
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)


# TODO 1: Write down what you think the output of do_it(5) will be
# Prediction:
# The do_it function calculates the sum of n % 2 (remainder when n is divided by 2) for n from 5 down to 1.
# Step-by-step:
# - do_it(5): 5 % 2 = 1, calls do_it(4) -> 1 + do_it(4)
# - do_it(4): 4 % 2 = 0, calls do_it(3) -> 0 + do_it(3)
# - do_it(3): 3 % 2 = 1, calls do_it(2) -> 1 + do_it(2)
# - do_it(2): 2 % 2 = 0, calls do_it(1) -> 0 + do_it(1)
# - do_it(1): 1 % 2 = 1, calls do_it(0) -> 1 + do_it(0)
# - do_it(0): n <= 0, returns 0
# Sum: 1 + 0 + 1 + 0 + 1 = 3
# Expected output of print(do_it(5)): 3

# TODO 2: Use the debugger to step through and see what's actually happening
# Debugging steps in PyCharm:
# 1. Open recursion.py and set a breakpoint by clicking in the gutter next to the line 'return n % 2 + do_it(n - 1)'.
# 2. Start the debugger by clicking the 'Debug' button (Shift+F9) and selecting recursion.py.
# 3. Use 'Step Into' (F7) to follow recursive calls or 'Step Over' (F8) to move to the next line.
# 4. In the 'Variables' pane, observe the value of 'n' decreasing from 5 to 0.
# 5. Watch the return values: 5 % 2 = 1, 4 % 2 = 0, 3 % 2 = 1, 2 % 2 = 0, 1 % 2 = 1, summing to 3.
# 6. Confirm the final output is 3, matching the prediction.
# Result: The debugger shows the function correctly returns 3, confirming the prediction.

print("do_it(5) output:")
print(do_it(5))


def do_something(n):
    """Print the squares of positive numbers from n down to 0.
    >>> do_something(2)
    4
    1
    0
    """
    if n < 0:
        return  # Stop recursion without printing
    print(n ** 2)  # Print the square of the current number
    do_something(n - 1)  # Recursive call to process the next number


# TODO 3: Write down what you think the output of do_something(4) will be
# Original function (before fix):
# def do_something(n):
#     """Print the squares of positive numbers from n down to 0."""
#     if n < 0:
#         print(n ** 2)
#     do_something(n - 1)
#
# Prediction for original do_something(4):
# - The original function only prints when n < 0, which contradicts the docstring ("positive numbers from n down to 0").
# - It lacks a proper base case to stop at n = 0, causing infinite recursion.
# - For n = 4, it calls do_something(3), then do_something(2), and so on, without printing until n < 0.
# - At n = -1, it prints (-1) ** 2 = 1, then continues to n = -2, -3, etc., until Python raises a RecursionError.
# Expected output of original: RecursionError due to infinite recursion.
#
# Prediction for fixed do_something(4) (current code):
# - The fixed function prints n ** 2 for n >= 0 and stops when n < 0.
# - Step-by-step:
#   - n = 4: Print 4 ** 2 = 16, call do_something(3)
#   - n = 3: Print 3 ** 2 = 9, call do_something(2)
#   - n = 2: Print 2 ** 2 = 4, call do_something(1)
#   - n = 1: Print 1 ** 2 = 1, call do_something(0)
#   - n = 0: Print 0 ** 2 = 0, call do_something(-1)
#   - n = -1: Return (stop)
# Expected output: 16, 9, 4, 1, 0 (each on a new line)

# TODO 4: Use the debugger to step through and see what's actually happening
# Debugging steps for do_something(4) in PyCharm:
# 1. Set a breakpoint on the line 'print(n ** 2)' in the do_something function.
# 2. Uncomment or ensure do_something(4) is called in the main block (already included below).
# 3. Start the debugger (Shift+F9) and select recursion.py.
# 4. Use 'Step Into' (F7) to follow recursive calls.
# 5. Observe 'n' decreasing from 4 to -1 in the 'Variables' pane.
# 6. Verify that squares (16, 9, 4, 1, 0) are printed for n = 4, 3, 2, 1, 0.
# 7. Confirm the function stops at n = -1 without errors.
# Result: The debugger shows the fixed function correctly prints 16, 9, 4, 1, 0, matching the prediction.

# TODO 5: Fix do_something() so that it works according to the docstring
# Issues with original do_something:
# - Printed n ** 2 only when n < 0, which is incorrect (should print for positive numbers and 0).
# - Lacked a proper base case, causing infinite recursion.
# Fixes applied:
# - Moved print(n ** 2) outside the base case to print for n >= 0.
# - Changed the base case to 'return' when n < 0, stopping recursion without printing.
# - Added doctests to verify do_something(2) prints 4, 1, 0.
# The fixed function now correctly prints the squares of positive numbers from n down to 0.

# Additional requirement: Write a version that recursively prints squares backwards
def do_something_reverse(n):
    """Print the squares of positive numbers from 0 up to n.
    >>> do_something_reverse(2)
    0
    1
    4
    """
    if n < 0:
        return  # Stop recursion
    do_something_reverse(n - 1)  # Recursive call first
    print(n ** 2)  # Print on the way back, giving reverse order


if __name__ == "__main__":
    print("do_it(5) output:")
    print(do_it(5))
    print("\ndo_something(4) output:")
    do_something(4)
    print("\ndo_something_reverse(4) output:")
    do_something_reverse(4)
    doctest.testmod()
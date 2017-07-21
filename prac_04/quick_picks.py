"""
CP1404/CP5632 Practical - Suggested Solution
Quick pick program
"""

import random

NUMBERS_PER_LINE = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    """Quick picks program - choose sets of random numbers."""
    quick_picks = int(input("How many quick picks? "))
    while quick_picks < 0:
        print("That makes no sense!")
        quick_picks = int(input("How many quick picks? "))

    for i in range(quick_picks):
        for j in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM, MAXIMUM)
            print("{:2}".format(number), end=' ')
        print()


main()

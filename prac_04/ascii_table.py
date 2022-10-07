"""
CP1404/CP5632 - Practical - Suggested Solution
ASCII table and converter, with functions
"""

LOWER = 33
UPPER = 127


def main():
    """Get and convert ASCII values/characters."""
    char = input("Enter a character: ")
    print(f"The ASCII code for {char} is {ord(char)}")
    number = get_number_between(LOWER, UPPER)
    print(f"The character for {number} is {chr(number)}")

    # ASCII table (no columns)
    for value in range(LOWER, UPPER + 1):
        print(f"{value:3} {chr(value):>4}")


def get_number_between(lower=LOWER, upper=UPPER):
    """Get a valid number between the given parameters."""
    number = int(input(f"Enter a number between {lower} and {upper}: "))
    while number < lower or number > upper:
        number = int(input(f"Enter a number between {lower} and {upper}: "))
    return number


main()

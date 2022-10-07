"""
CP1404/CP5632 - Practical - Suggested Solution
ASCII table and converter
"""
MAX_COLUMNS = 10
MIN_COLUMNS = 2

LOWER = 33
UPPER = 127

char = input("Enter a character: ")
print(f"The ASCII code for {char} is {ord(char)}")
number = int(input(f"Enter a number between {LOWER} and {UPPER}: "))
while number < LOWER or number > UPPER:
    number = int(input(f"Enter a number between {LOWER} and {UPPER}: "))
print(f"The character for {number} is {chr(number)}")

# ASCII table (single column)
for value in range(LOWER, UPPER + 1):
    print(f"{value:3} {chr(value):>4}")

# ASCII tables with columns (two versions)
number_of_columns = int(input("Enter number of columns: "))
while number_of_columns < MIN_COLUMNS or number_of_columns > MAX_COLUMNS:
    print(f"Please use a value between {MIN_COLUMNS} and {MAX_COLUMNS}")
    number_of_columns = int(input("Enter number of columns: "))
# calculate the range of values and the number of full rows
number_of_values = UPPER - LOWER + 1
number_of_rows = number_of_values // number_of_columns

print("Version 1: Horizontal then vertical ordering")
# iterate through the full rows first, incrementing by 1
value = LOWER
for row_number in range(number_of_rows):
    for column_number in range(number_of_columns):
        print(f"{value:6} {chr(value):>2}", end="")
        value += 1
    print()

# last row is special as it may not have all columns so handle separately
# start where we left off and only print up to UPPER
starting_value = value
for value in range(starting_value, UPPER + 1):
    print(f"{value:6} {chr(value):>2}", end="")
print("\n")

print("Version 2: Vertical then horizontal ordering")
# iterate through rows
for row_number in range(number_of_rows + 1):
    starting_value = LOWER + row_number
    value = starting_value
    # print all column values not including the last one (-1)
    for column_number in range(number_of_columns - 1):
        value_to_print = value + (column_number * number_of_rows)
        print(f"{value_to_print:6} {chr(value_to_print):>2}", end="")
        value += 1

    # last column may not exist so handle separately
    # having the if statement outside the for loop means we don't do it every column
    # so, it is more efficient (we can't avoid doing it every row AFAIK)
    value_to_print = value + ((column_number + 1) * number_of_rows)
    if value_to_print <= UPPER:
        print(f"{value_to_print:6} {chr(value_to_print):>2}", end="")
    print()

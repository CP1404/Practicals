"""
CP1404/CP5632 - Practical
Various examples of using Python string formatting with the str.format() method
Want to read more about it? https://docs.python.org/3/library/string.html#formatstrings
"""

name = "Gibson L-5 CES"
year = 1922
cost = 16035.4

# The ‘old’ manual way to format text with string concatenation:
print("My guitar: " + name + ", first made in " + str(year))

# A better way - using str.format():
print("My guitar: {}, first made in {}".format(name, year))
print("My guitar: {0}, first made in {1}".format(name, year))
print("My {0} was first made in {1} (that's right, {1}!)".format(name, year))

# Formatting currency (grouping with comma, 2 decimal places):
print("My {} would cost ${:,.2f}".format(name, cost))

# Aligning columns:
numbers = [1, 19, 123, 456, -25]
for number in numbers:
    print("Number is {:>5}".format(number))

# A version of the above loop using the enumerate function, useful when you want the index and value
for i, number in enumerate(numbers):
    print("Number {0} is {1:>5}".format(i + 1, number))

# TODO: Use string formatting to produce the output:
# 1922 Gibson L-5 CES for about $16,035!

print("{} {} for about ${:,.0f}!".format(year, name, cost))

# TODO: Using a for loop with the range function and string formatting,
# produce the following right-aligned output (do not use a list):
#   0
#  50
# 100
# 150

for number in range(0, 151, 50):
    print("{:3}".format(number))


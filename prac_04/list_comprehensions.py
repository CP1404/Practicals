"""
CP1404/CP5632 Practical
List comprehensions
"""

names = ["Bob", "Angel", "Jimi", "Alan", "Ada"]
full_names = ["Bob Martin", "Angel Harlem", "Jimi Hendrix", "Alan Turing",
              "Ada Lovelace"]

# for loop that creates a new list containing the first letter of each name
first_initials = []
for name in names:
    first_initials.append(name[0])
print(first_initials)

# list comprehension that does the same thing
first_initials = [name[0] for name in names]
print(first_initials)

# list comprehension that creates a list containing tuples of both initials
# splits each name and adds the first letter of each part to a tuple
full_initials = [(name.split()[0][0], name.split()[1][0]) for name in
                 full_names]
print(full_initials)

almost_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# TODO: use a list comprehension to create a list of integers
# from this list of strings
# numbers =

# TODO: use a list comprehension to create a list of all of the full_names
# in lowercase format
# lowercase_full_names =

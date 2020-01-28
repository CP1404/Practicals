"""
CP1404/CP5632 Practical Suggested Solution
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Read subject data and display neatly."""
    data = get_data()
    display_subjects(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        data.append(parts)
    input_file.close()
    return data


def display_subjects(data):
    """Display data nicely."""
    for subject_data in data:
        print("{} is taught by {:12} and has {:3} students".format(*subject_data))


main()

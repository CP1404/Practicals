"""
CP1404/CP5632 Practical
File and class example - opens/reads a file, stores in objects of custom class
(contains multiple versions for demonstration: using csv and namedtuple)
"""

import csv
from collections import namedtuple

from Prac08.programming_language import ProgrammingLanguage

__author__ = 'Lindsay Ward'


def main():
    """ read a file of programming language details, save as objects, display """
    languages = []
    # open the file for reading
    in_file = open('languages.csv', 'r')

    # format is like: Language,Typing,Reflection,Year
    # 'consume' the first line (header) - we don't need its contents
    in_file.readline()

    # all other lines are language data
    for line in in_file:
        # print(repr(line))  # debugging

        # strip newline from end and split it into parts (CSV)
        parts = line.strip().split(',')
        # print(parts)  # debugging

        # reflection is stored as a string (Yes/No) and we want a Boolean
        reflection = parts[2] == "Yes"

        # construct a ProgrammingLanguage object using the elements - year should be an int
        language = ProgrammingLanguage(parts[0], parts[1], reflection, int(parts[3]))

        # add the language we've just constructed to the list
        languages.append(language)

    # close the file as soon as we've finished reading it
    in_file.close()

    # loop through and display all languages (using their str method)
    for language in languages:
        print(language)

main()


def using_csv():
    # open the file for reading -
    # specify newline to avoid quoted \n in strings being considered a new record
    in_file = open('languages.csv', 'r', newline='')
    in_file.readline()
    reader = csv.reader(in_file)  # use default dialect, Excel
    for row in reader:
        print(row)

    in_file.close()

# using_csv()


def using_namedtuple():
    in_file = open('languages.csv', 'r', newline='')
    file_field_names = in_file.readline().strip().split(',')
    print(file_field_names)
    Language = namedtuple('Language', 'name, typing, reflection, year')
    reader = csv.reader(in_file)  # use default dialect, Excel

    for row in reader:
        # print(row)
        language = Language._make(row)
        print(repr(language))
    in_file.close()

# using_namedtuple()


def using_csv_namedtuple():
    Language = namedtuple('Language', 'name, typing, reflection, year')
    in_file = open("languages.csv", "r")
    in_file.readline()
    for language in map(Language._make, csv.reader(in_file)):
        print(language.name, 'was released in', language.year)
        print(repr(language))

# using_csv_namedtuple()



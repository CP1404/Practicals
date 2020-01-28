"""
CP1404/CP5632 - Practical - Suggested Solution
Convert temperatures between files
This also contains a function to create the data file to begin with
"""

import random


def main():
    """Convert input file of one temperature unit to output file of another unit."""
    # create_input_file(15)
    input_file = open("temps_input.txt", "r")
    output_file = open("temps_output.txt", "w")
    for line in input_file:
        result = convert_fahrenheit_to_celsius(float(line))
        # result = convert_celsius_to_fahrenheit(float(line))
        print(result, file=output_file)
    input_file.close()
    output_file.close()


def create_input_file(quantity):
    """Write number (quantity) of temperatures to file."""
    temperatures_file = open("temps_input.txt", "w")
    for i in range(quantity):
        temperature = random.uniform(-200, 200)
        print(temperature, file=temperatures_file)
    temperatures_file.close()


def convert_celsius_to_fahrenheit(celsius):
    """Convert celsius to fahrenheit."""
    return celsius * 9.0 / 5 + 32


def convert_fahrenheit_to_celsius(fahrenheit):
    """Convert fahrenheit to celsius."""
    return 5 / 9 * (fahrenheit - 32)


main()

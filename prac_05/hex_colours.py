"""
CP1404/CP5632 Practical - Suggested Solution
Hexadecimal colour lookup
"""

COLOUR_CODES = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7",
                "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc",
                "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378",
                "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6",
                "aquamarine4": "#458b74", "azure1": "#f0ffff",
                "azure2": "#e0eeee", "azure3": "#c1cdcd", "azure4": "#838b8b",
                "beige": "#f5f5dc", "bisque1": "#ffe4c4"}

colour_name = input("Enter a colour name: ")
while colour_name != "":
    # Note: using the get dictionary method
    # means you will get None if the key is not found
    print("The code for \"{}\" is {}".format(colour_name,
                                             COLOUR_CODES.get(colour_name)))
    colour_name = input("Enter a colour name: ")

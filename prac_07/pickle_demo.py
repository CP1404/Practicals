"""
CP1404/CP5632 Pickle and JSON Demo
This program demonstrates:
- Using JSON strings
- Using pickling to save and load variables in memory to and from a binary file
"""
import json
import pickle
from programming_language import ProgrammingLanguage

# JSON

# First, we start with this data string, stored in JSON format
# (it's a list of dictionary-like objects)
start_string = '[{"name": "Python", "typing": "Dynamic", "reflection": true, "year": 1991}, {"name": "Ruby", ' \
               '"typing": "Dynamic", "reflection": true, "year": 1995}] '
languages = json.loads(start_string)
print(languages, type(languages))

# Since these are dictionaries and not our ProgrammingLanguage objects,
# let's make objects from those values now
for i, language in enumerate(languages):
    # The following line unpacks the language dictionary using keyword argument
    languages[i] = ProgrammingLanguage(**language)
    # The following line unpacks the language dictionary values only,
    # which would require the order to match the constructor
    # languages[i] = ProgrammingLanguage(*language.values())

# We should now have a list variable called languages, which we can treat like any list
# Let's add another language to it
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
languages.append(visual_basic)

# Convert ("dump") our data in memory to a JSON string
# Note that we could have done this without ever having a JSON string to begin with
# default=vars specifies what to do when an object (like a ProgrammingLanguage) is not serialisable by default
json_string = json.dumps(languages, default=vars)
print("JSON string: ")
print(json_string)

# Pickling

# Convert ("dump") our data in memory to a pickled bytes object
# You don't usually want this,
# but it shows you something of what it's like when written to a file
pickle_string = pickle.dumps(languages)
print("Bytes object: ")
print(pickle_string)

# Write our data to a binary (not text) file
filename = input("Enter filename to write to: ")
# Notice the mode is "wb" - (w)rite (b)ytes
with open(filename, "wb") as out_file:
    pickle.dump(languages, file=out_file)

# Try loading the file you just saved... what does it look like?

# Now let's load the binary file into a new variable
print("Loading...")
with open(filename, "rb") as in_file:
    data = pickle.load(file=in_file)
print(data, type(data))

"""
CP1404/CP5632 Practical - Suggested Solution
Count word occurrences in a string
"""

unique_words = {}
text = input("Text: ")
# text = "this is a collection of words of nice words this is a fun thing it is"
words = text.split()
for word in words:
    frequency = unique_words.get(word, 0)
    # Note: this is the "Look Before You Leap" (LBYL) pattern
    # we could use the "Easier to Ask Forgiveness" pattern using exceptions
    unique_words[word] = frequency + 1

# Print the unique words and their frequencies,
# in alphabetical order
words = list(unique_words.keys())
words.sort()
# use the max function to find the maximum of the values produced by the
# generator function (like a list comprehension) of lengths of words
max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, unique_words[word]))

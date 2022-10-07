"""
CP1404/CP5632 Practical - Suggested Solution
Count word occurrences in a string
This example is in the lecture notes 3 different ways
"""

word_to_count = {}
text = input("Text: ")
# text = "this is a collection of words of nice words this is a fun thing it is"
words = text.split()
for word in words:
    # Note: this is the "Look Before You Leap" (LBYL) pattern
    # we could use the "Easier to Ask Forgiveness" (EAFP) pattern using exceptions
    frequency = word_to_count.get(word, 0)
    word_to_count[word] = frequency + 1

# Print the unique words and their frequencies,
# in alphabetical order
words = list(word_to_count.keys())
words.sort()

# use the max function to find the maximum of the values produced by the
# generator function (like a list comprehension) of lengths of words
max_length = max((len(word) for word in words))
for word in words:
    print("{word:{max_length}} : {word_to_count[word]}")

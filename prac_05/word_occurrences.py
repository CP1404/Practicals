"""
CP1404 Practical - Suggested Solution
Count word occurrences in a string
This example is in the lecture notes 3 different ways
"""

word_to_count = {}
# text = input("Text: ")
text = "this is a collection of words of nice words this is a fun thing it is"
words = text.split()
for word in words:
    # Note: this is the "Look Before You Leap" (LBYL) pattern
    # we could use the "Easier to Ask Forgiveness" (EAFP) pattern using exceptions
    frequency = word_to_count.get(word, 0)
    word_to_count[word] = frequency + 1

# Use the max function to find the maximum of the values produced by the
# generator expression (like a list comprehension) of lengths of words
max_length = max((len(word) for word in words))
# When we sort a dictionary like this we get a list of the keys in sorted order
for word in sorted(word_to_count):
    print(f"{word:{max_length}} : {word_to_count[word]}")

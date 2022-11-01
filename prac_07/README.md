# Practical 07 - Classes 2

Remember to do this prac (as usual now) in a **new branch**, then do a **pull request**, mentioning
the correct student to get a code review.  
Remember to check and do your code review when requested.

[Find the right student to mention here each week (different for each practical)](https://github.com/CP1404/Starter/wiki/Code-Review-Order#prac-6)

Let's run through the process again:

- Ensure that your `master` branch is up-to-date: **Merge** your PR on GitHub. This updates your `master` branch to
  contain the work from your last feedback branch.
- Locally, in PyCharm, **Checkout** your `master` branch.
- **Pull** to update your local `master` branch. This pulls in the changes from GitHub including the merge.
- (Double-check that you are on the `master` branch, not the feedback branch.)
- Create a new branch, `prac_07_feedback`.

Expectations and marking for this prac include **doing a code review** not just requesting one.  
Submit both your own PR URL where you **request** a review, and the PR URL of the code review you have done.  
We understand that this means someone else must have requested that you do a review.

# This prac is being updated currently. Try again shortly. Thank you.

...

# Walkthrough Example

This example program loads a number of "Programming Languages" from a file and saves them in objects using the class we
wrote recently.

Download 3 files from this folder. For now let's start with:

- [language_file_reader.py](language_file_reader.py) (the client program)
- [programming_language.py](programming_language.py) (the class)
- [languages.csv](languages.csv) (the data file)

Read the comments and the code in `language_file_reader.py` to see how it works.

Notice how:

- the file is opened and closed
- `readline()` is used to read (only) the first line, which just ignores the header in the CSV file
- a for loop is used to read the rest of the file
- reflection is stored in the file as a string, but this client code converts it to a Boolean ready for the class. It's
  not the class's job to do this conversion but the client's.
- There are also a few other versions included that use Python's `csv`
  module and a `namedtuple`. Read through to see how they work!

## Modifications

1. Add another language to the file - and make sure it still works properly. Use data from
   [this Programming Language Comparison page](http://www.jvoegele.com/software/langcomp.html)
2. Add another field to your ProgrammingLanguage class: **Pointer Arithmetic** (see that page or search to find if
   the language has it or not). This will be a Boolean variable.  
   This may take a bit of effort, as you need to update the class and any code that uses it. You also need to add the
   correct values to your data file (in a form similar to reflection).
3. Update any docstrings

# Intermediate Exercises

# Do-from-scratch Exercises

## More Guitars!

File: `myguitars.py`

Open the file: [guitars.csv](guitars.csv)  
This file contains lines like:

`Fender Stratocaster,2014,765.4`

So, the format/protocol is:

`Name,Year,Cost`

Write a program to read all of these guitars and store them in a list of `Guitar` objects,
using the class that you wrote recently.  
Display these using a loop.

Now **sort** the list by year (oldest to newest) and display them in sorted order...  
How do you do that?  
Sorting requires that Python knows how to compare objects...  
If we just use:

`guitars.sort()`

We get an error like:

`TypeError: unorderable types: Guitar() < Guitar()`

So we need to define how the `<` operator should work.  
Do you remember how?

Write code for the `__lt__` (less than) method. You should be able to figure this out...  
Then test and see if it sorts correctly now.

### Commit as you go

This is a good time for a commit. You haven't completed the whole task, but you've reached a "small milestone".  
Commit with an appropriate message using a capital and the imperative mood before moving on.  
You might write something like:

    Complete first part of More Guitars exercise

Now add to your program to ask the user
to enter their new guitars (just like your program from an earlier prac).  
Store these new guitars in your list of guitar objects, then  
write all of your guitars to the data file `guitars.csv`.

Test that this worked by opening the file, and also by running the program again to make sure it reads the new
guitars.

# Practice & Extension Work

How did you go with this section from the last prac?  
If you didn't complete all of that work, then go back and work on those exercises.

# Deliverables

This section summarises the expectations for marking in this practical.  
Please follow the [submission guidelines](../README.md#submission) to ensure you receive marks for your work.

This week, please submit two PR URLs:

- Your own feedback branch PR with a mention of a reviewer
- the PR that you reviewed. You need to do a **good** code review!

Files required:

- Practicals repository on GitHub and up-to-date (every week)
- `myguitars.py`
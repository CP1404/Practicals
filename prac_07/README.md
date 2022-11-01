# Practical 07 - Classes 2

Remember to do your work for this prac (as is usual now) in a **new branch**, then do a **pull request**, mentioning
the correct student to get a code review.  
Remember to check and do your code review when requested.

[Find the right student to mention here](https://github.com/CP1404/Starter/wiki/Code-Review-Order#prac-7)

Let's run through the process:

- **Merge** your PR on GitHub to ensure that your remote `master` branch is up-to-date.
  This updates your remote `master` branch to contain the work from your last feedback branch.
- In PyCharm, **Checkout** your local `master` branch.
- **Pull** to update your local `master` branch.
  This pulls in the changes from GitHub including the merge.
- (Double-check that you are on the `master` branch, not the feedback branch.)
- Create a new branch, `prac_07_feedback`.

Expectations and marking for this prac include both requesting and doing a code review.  
See submission details at the end of the prac.

# README

As you have seen, a "README" file is a common aspect of a software project.  
A good README usually introduces a project, provides details about the author, and includes any instructions needed for
someone else to benefit from your project.  
We will now add a README to our practicals repository.

New > File `README.md` (exact spelling) in your practicals main/root directory (not in prac_07 or similar).  
If you already have one, just edit it. You don't need to create a new one.  
PyCharm knows about markdown files, so it will give you syntax highlighting and other features as you type.

Include at least the following in your practicals README:

- Headings 1 and 2. These lines will start with `#` and `##` respectively. Use headings appropriately and semantically.
- Brief information about the repo and yourself.
- A list (markdown `-`) of at least 3 main lessons you have learned about "clean code" in this subject.
- Links to the Programming Patterns page and the CP1404 Practicals instructions repo.

Please "Reformat Code" to ensure your formatting is correct before you finish and commit your README.

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
2. Add another field to your `ProgrammingLanguage` class: **Pointer Arithmetic** (see that page or search to find if
   the language has it or not). This will be a Boolean variable.  
   This may take a bit of effort, as you need to update the class and any code that uses it. You also need to add the
   correct values to your data file (in a form similar to reflection).
3. Check that your code is complete including updating any docstrings.  
   Are `__str__` and other methods complete and good?

# Intermediate Exercises

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

Test that this worked by opening the data file, and also by running the program again to make sure it reads the new
guitars.

# Do-from-scratch Exercises

## Project Management Program

File: `project.py`  
File: `project_management.py`

Read the instructions, then enter a **time estimate** in your module docstring.

The instructions for this exercise are intentionally not step-by-step.  
We want you to use what you've learned about good program and class design, iterative development, version control,
clean code, etc. to determine the best approach.

Save the [projects.txt](projects.txt) data file to your prac folder.  
This file contains the data for this exercise delimited by tabs.  
The first line is a header, explaining the fields for each project.

Write a program in `project_management.py` to load and save a data file and use a list of `Project` objects.

Your program should contain a menu with the following options:

- Load projects  
  (Load projects when the program runs and also when they choose this option)
- Save projects  
  (Save projects when the program runs and also when they choose this option)
- Add new project  
  (Ask the user for the inputs and add a new project to memory)
- Display projects  
  (Display two groups: incomplete projects; completed projects, both sorted by priority)
- Show projects by time
  (Ask the user for a date and display all projects that start after that date)
- Update project  
  (Choose a project, then modify the completion % and/or priority)

### Expectations:

- Commit your work as you go (iterative development)
- Some of this could be considered relatively "hard" - do the easy bits first, then add more as you go
- Use the [datetime](https://docs.python.org/3/library/datetime.html) module for the project start date
- Write your class such that you are able to sort/compare `Project` objects based on priority order
- Write good clean code (no pylint warnings) with good naming and design (as always!)

Is this exercise to big? Will it take too long? Probably.  
Be systematic, thoughtful, use the patterns you've learned, copy from previous examples... be efficient.  
Not every student can do every task in every subject. Some things are challenging and that's OK.

# Practice & Extension Work

How did you go with this section from the last prac?  
If you didn't complete all of that work, then go back and work on those exercises.

# Deliverables

This section summarises the expectations for marking in this practical.  
Please follow the [submission guidelines](../README.md#submission) to ensure you receive marks for your work.

You may not receive your code review request in time to submit each week,
so we ask for the code review you did from the previous week.

This week, please submit two PR URLs:

- Your own feedback branch PR with a mention of a reviewer **for this prac**.
- The PR that you reviewed **for the last prac**.

Files required:

- Practicals repository on GitHub and up-to-date (every week)
- `README.md` (submitted and on GitHub, as with all the files)
- `language_file_reader.py`, `programming_language.py`, `languages.csv`
- `myguitars.py`
- `project`, `project_management.py`

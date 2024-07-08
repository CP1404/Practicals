# Practical 07 - Classes 2

Remember to do your work for this prac (as is usual now) in a **new branch**, then do a **pull request**, mentioning
the correct student to get a code review.  
Remember to check and do your code review when requested.

[Find the right student to mention here](https://github.com/CP1404/Starter/wiki/Code-Review-Order#prac-7)

You do not need to wait to receive your code review before starting.  
If you have not received a review, you can still complete this process. 
The PR URL is still the same and the reviewer can still review the code even though it has been merged.

Let's run through the process:

- **Merge** your PR on GitHub.  
  This updates your remote `master` branch to contain the work from your last feedback branch.
- In PyCharm, **Checkout** your local `master` branch.
- **Pull** to update your local `master` branch.
  This pulls in the changes from GitHub including the merge.
- (Double-check that you are on the `master` branch, not the feedback branch.)
- Create a new branch, `prac_07_feedback`.
- Do your prac work.

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

File: `guitar.py`  
File: `myguitars.py`

Start by copying `guitar.py` from your `prac_06` folder into this week's prac.  
We could import it, but we want to modify it, so we'll leave the old one unchanged.

Save the file: [guitars.csv](guitars.csv) to your prac folder.  
This file contains lines like:

`Fender Stratocaster,2014,765.4`

So, the format/protocol is:

`Name,Year,Cost`

Write a program to read all of these guitars and store them in a list of `Guitar` objects,
using the class that you wrote recently.  
Display these using a loop.  
Use a `main` and other appropriate functions.

Now **sort** the list by year (oldest to newest) and display them in sorted order...  
How do you do that?  
Sorting requires that Python knows how to compare objects...  
If we just use:

`guitars.sort()`

We get an error like:

`TypeError: unorderable types: Guitar() < Guitar()`

So we need to define how the `<` operator should work.  
Do you remember how?

Write code for the `__lt__` (less than) method so that it compares Guitars by year.    
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

Load projects from the default data file, `projects.txt`, when the program starts, before the menu.  
When the user quits, give them the choice of saving to the default file.  
Note that there are two menu options for loading from and saving to different files.

Your program should contain a menu with the following options:

- Load projects  
  (Prompt the user for a filename to load projects from and load them)
- Save projects  
  (Prompt the user for a filename to save projects to and save them)
- Display projects  
  (Display two groups: incomplete projects; completed projects, both sorted by priority)
- Filter projects by date  
  (Ask the user for a date and display only projects that start after that date, sorted by date)
- Add new project  
  (Ask the user for the inputs and add a new project to memory)
- Update project  
  (Choose a project, then modify the completion % and/or priority - leave blank to retain existing values)

### Expectations:

- Commit your work as you go (iterative development)
- Some of this could be considered relatively "hard" - do the easy bits first, then add more as you go
- Use the [datetime](https://docs.python.org/3/library/datetime.html) module for the project start date
- Write your class such that you are able to sort/compare `Project` objects based on priority order
- Think about writing utility/helper methods in your class and main program.  
  Think of our examples like `is_vintage` for Guitar and what you might use for a `Project`.
- Follow good design principles like SRP and DRY. Notice that there's two kinds of loading and write one function to
  handle both. Same for saving.
- Write good clean code (no pylint warnings) with good naming and design (as always!)

Here are two suggestions to leave until last (iterative development):

- Error checking. Do no error checking to start with.
- Date formatting. Just use a string until most everything else works, then, here are some suggestions.

The following code reads a string from user input, converts it to a `date` object (using the `strptime` method from
the `datetime` type), prints the day of the week (`%A`) and then prints the date as a string:

```python
import datetime

date_string = input("Date (d/m/yyyy): ")  # e.g., "30/9/2022"
date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
print(f"That day is/was {date.strftime('%A')}")
print(date.strftime("%d/%m/%Y"))
```

Remember to enter your **actual time** in your module docstring.  
Are you getting better at estimating?

Is this exercise too big? Will it take too long? Probably.  
Not every student can do every task in every subject. Some things are challenging and that's OK.

Be systematic, thoughtful, use the patterns you've learned, copy from previous examples... be efficient.  
Don't waste time reinventing new/different ways to do
"standard" things like menus. Follow the patterns.

### Sample output

    Welcome to Pythonic Project Management
    Loaded 5 projects from projects.txt
    - (L)oad projects  
    - (S)ave projects  
    - (D)isplay projects  
    - (F)ilter projects by date
    - (A)dd new project  
    - (U)pdate project
    - (Q)uit
    >>> d
    Incomplete projects: 
      Organise Pantry, start: 20/07/2022, priority 1, estimate: $25.00, completion: 55%
      Build Car Park, start: 12/09/2021, priority 2, estimate: $600000.00, completion: 95%
      Mow Lawn, start: 31/10/2022, priority 3, estimate: $3.00, completion: 0%
      Record Music Video, start: 01/12/2022, priority 9, estimate: $250000.00, completion: 0%
    Completed projects: 
      Read 7 Habits Book, start: 13/12/2021, priority 6, estimate: $99.00, completion: 100%
    - (L)oad projects  
    - (S)ave projects  
    - (D)isplay projects  
    - (F)ilter projects by date
    - (A)dd new project  
    - (U)pdate project
    - (Q)uit
    >>> u
    0 Build Car Park, start: 12/09/2021, priority 2, estimate: $600000.00, completion: 95%
    1 Mow Lawn, start: 31/10/2022, priority 3, estimate: $3.00, completion: 0%
    2 Organise Pantry, start: 20/07/2022, priority 1, estimate: $25.00, completion: 55%
    3 Record Music Video, start: 01/12/2022, priority 9, estimate: $250000.00, completion: 0%
    4 Read 7 Habits Book, start: 13/12/2021, priority 6, estimate: $99.00, completion: 100%
    Project choice: 3
    Record Music Video, start: 01/12/2022, priority 9, estimate: $250000.00, completion: 0%
    New Percentage: 20
    New Priority: 
    - (L)oad projects  
    - (S)ave projects  
    - (D)isplay projects  
    - (F)ilter projects by date
    - (A)dd new project  
    - (U)pdate project
    - (Q)uit
    >>> a
    Let's add a new project
    Name: Practical 7
    Start date (dd/mm/yy): 1/11/2022
    Priority: 1
    Cost estimate: $0
    Percent complete: 32
    - (L)oad projects  
    - (S)ave projects  
    - (D)isplay projects  
    - (F)ilter projects by date
    - (A)dd new project  
    - (U)pdate project
    - (Q)uit
    >>> f
    Show projects that start after date (dd/mm/yy): 20/7/2022
    Organise Pantry, start: 20/07/2022, priority 1, estimate: $25.00, completion: 55%
    Mow Lawn, start: 31/10/2022, priority 3, estimate: $3.00, completion: 0%
    Practical 7, start: 01/11/2022, priority 1, estimate: $0.00, completion: 32%
    Record Music Video, start: 01/12/2022, priority 9, estimate: $250000.00, completion: 20%
    - (L)oad projects  
    - (S)ave projects  
    - (D)isplay projects  
    - (F)ilter projects by date
    - (A)dd new project  
    - (U)pdate project
    - (Q)uit
    >>> u
    0 Build Car Park, start: 12/09/2021, priority 2, estimate: $600000.00, completion: 95%
    1 Mow Lawn, start: 31/10/2022, priority 3, estimate: $3.00, completion: 0%
    2 Organise Pantry, start: 20/07/2022, priority 1, estimate: $25.00, completion: 55%
    3 Record Music Video, start: 01/12/2022, priority 9, estimate: $250000.00, completion: 20%
    4 Read 7 Habits Book, start: 13/12/2021, priority 6, estimate: $99.00, completion: 100%
    5 Practical 7, start: 01/11/2022, priority 1, estimate: $0.00, completion: 32%
    Project choice: 0
    Build Car Park, start: 12/09/2021, priority 2, estimate: $600000.00, completion: 95%
    New Percentage: 100
    New Priority: 3
    - (L)oad projects  
    - (S)ave projects  
    - (D)isplay projects  
    - (F)ilter projects by date
    - (A)dd new project  
    - (U)pdate project
    - (Q)uit
    >>> d
    Incomplete projects: 
      Organise Pantry, start: 20/07/2022, priority 1, estimate: $25.00, completion: 55%
      Practical 7, start: 01/11/2022, priority 1, estimate: $0.00, completion: 32%
      Mow Lawn, start: 31/10/2022, priority 3, estimate: $3.00, completion: 0%
      Record Music Video, start: 01/12/2022, priority 9, estimate: $250000.00, completion: 20%
    Completed projects: 
      Build Car Park, start: 12/09/2021, priority 3, estimate: $600000.00, completion: 100%
      Read 7 Habits Book, start: 13/12/2021, priority 6, estimate: $99.00, completion: 100%
    - (L)oad projects  
    - (S)ave projects  
    - (D)isplay projects  
    - (F)ilter projects by date
    - (A)dd new project  
    - (U)pdate project
    - (Q)uit
    >>> q
    Would you like to save to projects.txt? no, I think not.
    Thank you for using custom-built project management software.

# Ready for Kivy?

Next week, we will be writing and running programs with the **Kivy** GUI toolkit.

Please test you can run successfully [this test code](https://github.com/CP1404/Starter/blob/master/check_setup.py).

If you cannot run the above code, please complete the setup this week:  
[Follow these instructions](https://github.com/CP1404/Starter/wiki/Software-Setup)

# Practice & Extension Work

How did you go with this section from the last prac?  
If you didn't complete all of that work, then go back and work on those exercises.

## Extension

"[Pickling](https://docs.python.org/3/library/pickle.html) is the process whereby a Python object hierarchy is converted
into a byte stream, and “unpickling” is the inverse operation, whereby a byte stream (from a binary file or bytes-like
object) is converted back into an object hierarchy."

You can use Python's `pickle` module to load and save data from files without having to manually process data.  
You essentially just "save" your variables in memory to a file.

Study [the provided pickling demo](pickle_demo.py) to see how to use pickling and JSON to load and dump objects to and
from memory.

Now, write a new version of the Project Management Program to use pickling to load and save the data.

# Deliverables

This section summarises the expectations for marking in this practical.  
Please follow the [submission guidelines](../README.md#submission) to ensure you receive marks for your work.

- Type the URL of your Pull Request (PR) that mentions another student **for this prac**.
- Type the URL of the PR that you reviewed **for the previous prac**.
- `README.md` (submitted and on GitHub, as with all the files)
- `language_file_reader.py`, `programming_language.py`, `languages.csv`
- `guitar.py`, `myguitars.py`
- `project.py`, `project_management.py`

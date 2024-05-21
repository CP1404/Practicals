# Practical 04 - Lists

# Warm-Up

File: `lists_warmup.py`

In your `prac_04` directory, create a new Python file called `lists_warmup.py` and enter the following line:

`numbers = [3, 1, 4, 1, 5, 9, 2]`

**What values do the following expressions have?**
Without running the code, record your answers to these questions in your Python file as a comment.  
Then use the Python console to see if you were correct.

    numbers[0]
    numbers[-1]
    numbers[3]
    numbers[:-1]
    numbers[3:4]
    5 in numbers
    7 in numbers
    "3" in numbers
    numbers + [6, 5, 3]

In the same Python file, write statements to achieve the following:

1. Change the first element of numbers to `"ten"` (the string, not the number `10`)
2. Change the last element of numbers to `1`
3. Print all the elements from numbers except the first two (slice)
4. Print whether `9` is an element of numbers

# Walkthrough Example

## Calculating a List of Cumulative Totals

*Please read the whole question before starting the work!*

Accountant Annie wants you to write a program to calculate the monthly
cumulative totals for incomes.  
The program should ask for the number of monthly incomes to enter, then
get and store the incomes in a list.

When the incomes have been entered, the program should display a list of
the month's income with cumulative totals.  
Here's some sample output (for 5 months in this case):

    How many months? 5
    
    Enter income for month 1: 120
    Enter income for month 2: 245.4
    Enter income for month 3: 900
    Enter income for month 4: 1205.56
    Enter income for month 5: 12.35

    Income Report
    -------------    
    Month  1 - Income: $    120.00         Total: $    120.00
    Month  2 - Income: $    245.40         Total: $    365.40
    Month  3 - Income: $    900.00         Total: $   1265.40
    Month  4 - Income: $   1205.56         Total: $   2470.96
    Month  5 - Income: $     12.35         Total: $   2483.31

Think about how to do this before reading on...

We need a **list** to store the incomes.  
How do you add values to a list?

We need a counter variable (int) for the month number.  
Remember that list indexes start at 0, but we want to print from 1.

How many loops will we need? What kind of loops?

We need a cumulative total to update as we loop through the list to display the incomes.

And lastly we need to format the output nicely, which we can use f-strings for.

### Things to do:

1. Copy the starter code from [total_income.py](total_income.py)
   (remember to use *Raw* mode) and commit it to your own prac repo:

2. Study it to see how this code answers those questions so far.

3. Change the line that gets the income input so that it uses an f-string instead of string concatenation (`+`).

4. **Problem**: We have two variables that sound very similar: `incomes` and
   `months`. They're both plural, so they sound like they're both
   lists. `incomes` is a list of incomes, so we might assume that `months`
   is a list of months, but it's actually a scalar value that stores
   the **number of months** - an `int` not a `list`.  
   **Refactor the** `months` **variable to a better name**.  
   DO NOT just change it in 3 places or use find and replace... but
   **use refactoring** in PyCharm by clicking anywhere on the variable and
   pressing Shift+F6 (or use the context menu). Then rename it to something
   more meaningful, that sounds like a number not a list.  
   When naming **variables**, we can say, _"This variable stores..."_ and
   the completion of that statement is usually a good name.  
   In this case, "This variable stores the... number of months". :)

5. Run the program again with some sample data and make sure it still works.  
   This kind of "regression testing" is important. Make sure you don't break anything!

6. Now, let's refactor (move) the report printing into its own
   function. Select those 6 lines and turn them into a new function
   with a good name.  
   When naming **functions**, we can say, "This function will..." and
   the completion of that statement is usually a good name for the function.  
   In this case, "This function will... print report". :)

7. Test again and make sure it's all good.

8. Double-check the report printing function you just wrote. Is it well-designed according to SRP? Does it take in _
   only_ what it needs to know? Refactor it if you can make it better.

## Converting Data Strings to Lists

A common way of storing data is in files, which means the data is in string form. Even numbers are stored as string.  
So, a data file storing subjects, lecturer and student numbers might look like:

    CP1401,Ada Lovelace,192
    CP1404,Alan Turing,98 

We can read a file like this line-by-line (`for line in file`) but we also need to
**process** each line to get the parts. A good way to do that is with the string `split` method.  
So, `line.split(',')` would give us a list that contained the parts of this line...
but each part would still be a string.

### Things to do:

1. Copy the starter code and data file from [subject_reader.py](subject_reader.py)
   and [subject_data.txt](subject_data.txt)    
   Remember to commit these before modifying them any further.   
   Study the starter code and run it. There are comments and `print` calls to show you what's happening.

2. The code reads the file data and processes it into the `parts` variable, but we want the `load_data` function
   to `return` the data as a list of lists (nested list), like:  
   `[['CP1401', 'Ada Lovelace', 192],['CP1404', 'Alan Turing', 98]]`  
   Modify the function so that it does this.
   
3. Currently, main just prints `data`. Add a new function to display subject details that
   produces something like the following:

       CP1401 is taught by Ada Lovelace and has 192 students
       CP1404 is taught by Alan Turing  and has  98 students

# Intermediate Exercises

Here are some small problems to give you more practice working with
lists.  
Feel free to **check the solutions** for these so that you can make sure you're on track.

## Basic list operations

File: `list_exercises.py`

Write a program that prompts the user for 5 numbers and then stores
each of these in a list called `numbers`.  
The program should then output information about these numbers, as in the output below.  
You can use the **functions** `min`, `max`, `sum` and `len`, and
you can use the `append` **method** to add a number to a list.

       Number: 5
       Number: 20
       Number: 1
       Number: 2
       Number: 3
       The first number is 5
       The last number is 3
       The smallest number is 1
       The largest number is 20
       The average of the numbers is 6.2

## Woefully inadequate security checker

Please use the same file, `list_exercises.py`

Copy the following list of usernames:

       usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob'] 

Ask the user for their username. If the username is in the above
list of authorised users, print "Access granted", otherwise print
"Access denied".

## List comprehensions

File: `list_comprehensions.py`

Download/copy [list_comprehensions.py](list_comprehensions.py)  
and see how the example list comprehensions work.  
Write more list comprehensions (not loops) by completing the `TODO` instructions in the code.

# Do-from-scratch Exercises

## "Quick Pick" Lottery Ticket Generator

File: `quick_picks.py`

Write a program that asks the user how many "quick picks" they wish to
generate. The program then generates that many lines of output. Each
line consists of 6 random numbers between 1 and 45.  
These values should be stored as `CONSTANTS`.

- Each line (quick pick) should not contain any repeated number.
- Each line of numbers should be displayed in sorted (ascending) order.
- Study the formatting below so that numbers align neatly.

> [!NOTE]
> Python's `random` module has a `sample()` function, which
> returns a selection from a list.  
> This is a nice way to solve this problem... but it's too easy :)  
> Do not use it for this program.

Your code should produce output that matches this sample output
(except the numbers are random):

    How many quick picks? 5
     1 12 14 15 30 36
     2  5  8 33 38 41
     2 12 19 22 29 43
    13 21 28 29 42 43
     3  4 10 11 32 44

# Practice & Extension Work

We know from many years of teaching programming, that to get good at this, you need to spend
lots of time writing programs, so here's some more to write.

## Practice

1. (If you haven't already)  
   Refactor the report function in `total_income.py` to use `enumerate`.  
   Any time you need _both_ the index and value from a list, enumerate is a useful function.
   In the original version, we already had the variable for the number of months,
   but after we refactored to make this report function, we don't need to pass two variables.  
   Why not? The number of months is just the length of the list...

2. Extend the first intermediate exercise (`list_exercises.py`) so that the user can enter
   any number of numbers until a number less than zero is entered.
   Adjust the prompt so that it prints like "Number 1: " then "Number 2: "...

3. Write a program that asks the user for an indefinite set of
   strings - until an empty string is entered - then prints all of the
   strings that were entered more than once.  
   E.g. if the user entered: "hello", "world is good", "hello", "john",
   "good world"... the program would print "Strings repeated: hello".  
   If no repeated strings are entered, the program should print "No
   repeated strings entered".

4. Memberwise Addition...  
   In Python, the + operator concatenates lists, so for example:  
   `[1, 2, 3] + [4, 5, 6] = [1, 2, 3, 4, 5, 6]`  
   What if we want to add the elements together instead?  
   Write a function, `add_memberwise`, that takes two lists, and
   returns the list that contains the sum of elements that are in the
   same index in the two lists. For example:  
   `add_memberwise([1, 2, 3], [4, 5, 6])` would return `[5, 7, 9]`  and  
   `add_memberwise([1, 2, 3], [1, 2, 3, 4])` would return `[2, 4, 6, 4]`

## Extension

1. Download the scores reading program: [scores.py](scores.py) and its data file: [scores.csv](scores.csv)

   The data file stores the scores for each subject for 10 people.  
   This code reads the lines into lists, saves the first line as a list
   of subject codes and converts the rest of the lines from a list of
   strings into a list of numbers, which it then prints with the
   maximum value for that subject. Nice... Except, it's broken! It
   reads the lists per user not per subject, so the results are
   incorrect.

   a. Save the CSV file to your project folder and copy the code into a
   new file and run it to see how it currently works.

   b. Can you fix it so that it prints the list of (10) scores per
   subject with the maximum per subject?

   c. When you've done that, also print the minimum and average for
   each subject.

   d. Then print the results in a nicely-formatted table.

2. Download/copy the sorting demonstration: [sorting.py](sorting.py)  
   Study how this works and complete the `TODO` instructions.

3. Copy your **word generator** program into another file. Commit.  
   Add error-checking so that you repeatedly validate the user's input
   until it is a valid sequence of just c's and v's. Create and use a
   function `is_valid_format(...)` to return True or False for if
   the word format is valid or not.  
   **Tip:** use a for loop to iterate through each character in the
   format sequence and return false if you see one that is not valid.

4. Copy your `ascii_table.py` file from last week's prac into this
   week's folder.  
   Create a function called `get_number(lower, upper)` to get a
   number, making sure that user input is numeric and within the given
   range.  
   You can use exceptions to check the string is a valid number.  
   Repeatedly re-prompt for a number until a valid one is entered, then
   return it.  
   Example:

       Enter a number (10-50):  
       >>>abc  
       Please enter a valid number!  
       Enter a number (10-50):  
       >>>75  
       Please enter a valid number!  
       Enter a number (10-50):  
       >>>30
       (then the function should return 30)

   When this function works, use it in your program in place of the code
   you used to get the number.  
   Test it with both invalid and valid inputs.

## Solutions to Selected Exercises

Remember that we have many solutions available in the solutions branch of the
Practicals repository. Change the branch on GitHub to solutions, or visit:  
<https://github.com/CP1404/Practicals/tree/solutions>

Remember also that the solutions are there to help you learn ***after***
you have done your best to complete the tasks on your own and using the
teaching resources we have provided.

# Deliverables

This section summarises the expectations for marking in this practical.  
Please follow the [submission guidelines](../README.md#submission) to ensure you receive marks for your work.

- Type the URL of your GitHub practicals repository in the text box when you submit your practical.
- `lists_warmup.py`
- `total_income.py`
- `subject_reader.py`
- `list_exercises.py`
- `list_comprehensions.py`
- `quick_picks.py`

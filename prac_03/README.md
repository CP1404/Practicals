# Practical 03 - Files, Exceptions

Now that you know how to use version control (Git and GitHub), please use it
consistently for **all** your work. This should just be how you normally work now.  
Remember that it's an important "industry-relevant" skill that you should expect to use
for many years to come (your entire IT career), so make the time to get good at it.

If you do not already have your prac work with you, start by **cloning**
your prac repository via PyCharm.

Each time you finish a practical task, **commit** it.

You only need to **push** once (when you finish and/or it's time to leave),
but you can do it more often if you wish.

When you're about to make a change, like refactoring, commit first so that you
can track the differences, and you can go back to a previous version if
you need to.

> [!IMPORTANT]
> Do Not make a new project for each practical.  
> Keep using the same PyCharm project and GitHub repo for all practicals.  
> If you need to work on a new computer, you can **clone** your repo.

# Walkthrough Example

## String Formatting

File: `string_formatting.py`

String formatting lets us format strings using format specifiers in a way that's very powerful and will make a lot
of sense once you get used to it.

Sometimes the best way to start learning this sort of thing is to see
some useful examples, so:

- Create a new Python file called `string_formatting.py` in
  your `prac_03` folder.

- (Remember when copying code from GitHub to use **Raw** so
  that the formatting copies properly.)  
  Copy the following string formatting examples from
  [string_formatting_examples.py](string_formatting_examples.py)
  into your file and run the code. (It's also written below for your
  reference.)

### Things to Notice

- Use the string formatting
  'mini language'; details come after the **:**  See: <https://docs.python.org/3/library/string.html#formatstrings>

- f-strings are not a complete replacement for `.format()`. There are some reasons to continue using `.format()` (such
  as with variable unpacking) so you should know both. Many Python programmers prefer f-strings for string formatting
  for readability and conciseness.

- The part *after* the colon specifies the formatting. E.g., `{:3}` specifies
  to use a width of 3 (or more if needed) for the value.

- By default, **numbers are right-aligned** and **strings are
  left-aligned**. You can change this with > or <  
  So, `{:>6}` would format the value to be right-aligned and take up 6 (or
  more if needed) spaces.

### Things to do

Use f-string formatting to produce the output:  
(Notice where the values go and also the float formatting / number of decimal places.)

```
1922 Gibson L-5 CES for about $16,036!
```

Using a `for` loop with the `range` function and **f-string formatting**, produce the following output.  
Do not use a list and notice that both variable numbers are right-aligned:

    2 ^ 0 is    1
    2 ^ 1 is    2
    2 ^ 2 is    4
    2 ^ 3 is    8
    2 ^ 4 is   16
    2 ^ 5 is   32
    2 ^ 6 is   64
    2 ^ 7 is  128
    2 ^ 8 is  256
    2 ^ 9 is  512
    2 ^10 is 1024

## Random Numbers

File: `randoms.py`

Python has a number of random functions -
contained within the `random` module. Unlike the built-in functions
(`print()`, `input()`, etc.) the random functions are *not* built-in
but need to be **imported**. Modules are reusable collections of
functions, classes and variables (constants) related to a specific topic
(e.g., maths, operating system services, handling dates and times).
Python has a useful built-in function for finding out about the local
scope of something, called `dir()`.

**Launch a Python Console** (in PyCharm, simply click in the
footer/status bar where it says "Python Console") and type the following
at the `>>>` prompt:

    dir(str)

This displays everything contained in `str`, like:

    ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

You can see all of those useful methods such as
`upper()`, `startswith()`, `isdecimal()`.

Next try running the `dir()` function with `random` as the argument:

    dir(random)

The result won't be quite the same...

    Traceback (most recent call last):
      File "<input>", line 1, in <module>
    NameError: name 'random' is not defined

This doesn't work, since random is a **module** that needs to be
**imported** first.

Now try it like this:

    import random
    dir(random)

This shows all the names in the module - most of which are
functions you can use. To use functions from a module that's been
imported like this you need to *qualify* the name - e.g., use
`random.randint` not just `randint`. Use `help()` to find out
about a couple of these functions:

    help(random.randint)
    Help on method randint in module random:
    randint(a, b) method of random.Random instance
        Return random integer in range [a, b], including both end points.
    
    help(random.randrange)
    Help on method randrange in module random:
    randrange(start, stop=None, step=1, _int=<class 'int'>) method of random.Random instance
        Choose a random item from range(start, stop[, step]).
        
        This fixes the problem with randint() which includes the
        endpoint; in Python this is usually not what you want.

The name of a function can be used without the brackets here, but this
does not execute the function.

**Never** name a file the same as a module;
e.g., `random.py` or it will have higher precedence when you import it.

In your **console**, type in the following (run each line multiple
times), and write the answers to the questions below in comments in `randoms.py`.

```python
import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3
```

- *What did you see on line 1?*  
  What was the smallest number you could have seen, what was the
  largest?

- *What did you see on line 2?*  
  What was the smallest number you could have seen, what was the
  largest?  
  *Could line 2 have produced a 4?*

- *What did you see on line 3?*  
  What was the smallest number you could have seen, what was the
  largest?

- Write code, not a comment, to produce a random number between 1 and 100 inclusive.

## Capitalist Conrad

File: `capitalist_conrad.py`

Download the code from: [capitalist_conrad.py](capitalist_conrad.py)

Capitalist Conrad wants us to write a stock-price simulator for a
volatile stock. The price starts off at $10.00, and, at the end of
every day there is a 50% chance it increases by 0 to 10%, and a 50%
chance that it decreases by 0 to 5%. If the price rises above $1000, or
falls below $0.01, the program should end. The price should be
displayed to the nearest cent (e.g., `$33.59`, not `$33.5918232901`).

**What module do we need to import?** `random`

**What functions from random do we need to use?** `randint` (for the 50%
chance of increase or decrease), and `uniform` (to generate a random
floating-point number)

### Things To Do

1. The program currently runs without telling us how many days it
   simulated.  
   Add this feature using a `number_of_days` variable so that
   the program prints like:

       Starting price: $10.00  
       On day 1 price is: $9.89  
       ...  
       On day 424 price is: $915.71  
       On day 425 price is: $1,001.60  

2. Notice how the use of `CONSTANTS` makes the program easier to read and customise.  
   Change these so that the allowed price range is $1 to $100 and
   the increase could be up to 17.5% (remember to change any comments
   that refer to constant values).   
   Run the program with these new values.

3. Update your program so that it writes the output to a **file**.

    - First you need to `open` the file for writing. You only need
      to do this once, so add this line before your loop starts:

      `out_file = open(FILENAME, 'w')`

      Note that this code line expects you to define the constant
      `FILENAME`, so do that above.

    - Update any print statements, so they output to the file.  
      Here's an (incomplete) example:

      `print(f"${price:,.2f}", file=out_file)`

    - **Close** the file at the very end:

      `out_file.close()`

## Exceptions Demo

File: `exceptions_demo.py`

Copy this example code that uses exceptions: [exceptions_demo.py](exceptions_demo.py)
and run it, then answer the following questions in comments in your file...

### Questions

1. When will a `ValueError` occur?
2. When will a `ZeroDivisionError` occur?
3. Could you change the code to avoid the possibility of a `ZeroDivisionError`?

If you could figure out the answer to question 3, then **make this change now**.

# Intermediate Exercises

## Exceptions To Complete

File: `exceptions_to_complete.py`

Let's write a program that gets an integer from the user and does not
crash when a non-number is entered. Copy the code from
[exceptions_to_complete.py](exceptions_to_complete.py)
and complete the program by following the `TODO` comment instructions.

> [!NOTE]
> PyCharm will probably give you a warning that `result` "may be undefined". This is safe to ignore.  
> It's not a PEP8 formatting warning.  
> It's PyCharm thinking that you might somehow exit the loop before defining `result`.  
> Since we are controlling how we exit the loop, we know that this problem will not occur.

*You're doing well. Keep it up...*

## Password Checker

File: `password_checker.py`

Download the starter code (complete with hints in the form of `TODO`
comments) from [password_checker.py](password_checker.py)

Write a program that asks for and validates a person's password. The
program is not for comparing a password to a known password, but
validating the 'strength' of a new password, like you see on websites:
enter your password, and then it tells you if it's valid (matches the
required pattern) and re-prompts if it's not.  
All passwords must contain **at least one** each of:

- digit
- lowercase letter
- uppercase letter

The starter code uses constants to store:

1. the minimum and maximum length of the password
2. whether a special character is required (note the Boolean naming)
3. the special characters (as a string; a list is not necessary)

Remember when a program has CONSTANTS, you should use them everywhere you can so that if you change them at the top,
this change affects the whole program as expected.  
E.g., if you changed the minimum length to 5, the program should print 5 and should check to make sure the password
is >= 5 characters long.

### Sample Output

Your output should look something like this:

    Please enter a valid password
    Your password must be between 5 and 15 characters, and contain:
        1 or more uppercase characters
        1 or more lowercase characters
        1 or more numbers
        and 1 or more special characters:  !@#$%^&*()_-=+`~,./'[]<>?{}|\
    > this?
    Invalid password!
    > whyNot?CanIhaveThis?
    Invalid password!
    > 12345678901234567890aBcv@
    Invalid password!
    > thisISmy123Pass!
    Invalid password!
    > 1thisISit!
    Your 10 character password is valid: 1thisISit!

Here's another run with the same code but different values for the
constants (special characters are not required in this version):

    Please enter a valid password
    Your password must be between 2 and 6 characters, and contain:
        1 or more uppercase characters
        1 or more lowercase characters
        1 or more numbers
    > aB
    Invalid password!
    > HowCanIHave2Chars?
    Invalid password!
    > 1aB
    Your 3 character password is valid: 1aB

Do not just try and Google "Python password checker" or something, but think about doing this step by step.  
We have provided a suitable structure for you with `TODO` comments in the code provided.  
Follow these.

- First, just check if a string has at least one lowercase character.  
  You can do this by looping through the string (`for character in password:`) and testing each character... count the
  ones that match (using `character.islower()`)...    
  At the end you know how many lowercase characters there are.

- Only when you are able to count lowercase, then, **in the same loop**,
  count the uppercase characters  
  That is, **do not** try and get all the checks working before you
  know that the first one works. **Do** one at a time.

- *Then*, count the numbers...  
  Test your code for each of these changes as you write them.

- For special characters, remember you can use the `in` operator to
  see if the character is `in` another string (our `SPECIAL_CHARACTERS` constant).

- ... keep going until you can tell how many of each kind of character there are.

- Then put it all together and test with some different settings.

**We hope that you use this incremental approach regularly.**

# Do-from-scratch Exercises

## Files

File: `files.py`

The solutions for these programs are provided, to help confirm that your solution was valid.

When you execute a Python program that contains a line like
`open('data.txt', 'w')` the new file "data.txt" is created in the
same folder as the Python file in your PyCharm project.

Create a new file called `files.py` and do all the following *separate questions* in it:  
The intention here is to give you experience using different ways to read files.  
Make the appropriate choice of file-reading technique for each of these questions:

- `read()`
- `readline()`
- `readlines()`
- `for line in file`

1. Write code that asks the user for their name, then opens a file
   called `name.txt` and **writes** that name to it. Use `open` and `close` for this question.

2. In the same file, but as if it were a separate program, write code that opens "name.txt" and reads the name (as
   above)
   then prints (note the exact output),  
   `Hi Bob!` (or whatever the name is in the file). Do not simply print the user's input variable!  
   Use `open` and `close` for this question.

3. Create a text file called `numbers.txt` and save it in your prac directory. Put the following three numbers on
   separate lines in the file
   and save it:  
   17  
   42  
   400  
   Write code that opens `numbers.txt`, reads **only** the first two numbers, adds
   them together then prints the result, which should be... 59.
   Use `with` instead of `open` and `close` for this question.

4. Now write a fourth block of code that prints the total for **all lines** in `numbers.txt`.
   This should work for a file with *any* number of numbers.
   Use `with` instead of `open` and `close` for this question.

Remember that understanding and choosing "the right tool for the job" is a primary focus for you as a programmer.   
In the questions above, you should have used `read`, `readline` and `for line in file` for reading.

## .gitignore

![GitHub logo](../images/githublogo.png)  
Before we're done, let's learn one more Git thing: **ignoring** files.  
If you created your project from our template repository, then you already have this file, so there's no more to do.  
The following details are here to help you understand how `.gitignore` works.  
If you did not use the template, then you need to do this manually now...

You have files in your project that you don't want stored in your
repo, like PyCharm metadata files. You can just choose not to add them
(as we've done until now) but they do show up as "unversioned files".   
We'd prefer to only see files we should consider adding.

![Unversioned Files window](../images/04image2.png)

The solution is to use a file called `.gitignore` in your repository.  
Note the exact spelling, including the dot at the start and no extension.  
On Unix-like systems (including Mac), the dot makes a file/folder _hidden_.

`.gitignore` is just a plain text file that stores the names of any files or
folders you want Git not to track and not to warn you about.  
Your file will still exist in your _project_, but not in your _repository_.

(If you don't already have one)  
**Create a file called `.gitignore`** in the **root folder** (NOT inside a subfolder) of your project,
and **add** it to Git.

Then enter the following line (the trailing slash means it will match a directory
but not a file with that name):

    .idea/

`.idea` is the directory (folder) that PyCharm stores its project metadata in.

Now look at that Version Control tool window... problem solved!

![No unversioned files](../images/04image3.png)

Commit and Push.

If you had already committed your `.idea` folder to your
repository, PyCharm does not seem to provide a way to stop tracking this.
You use the Git command line (e.g., in PyCharm's Terminal, git bash, or Mac Terminal).  
Ask your tutor if you've never done this before.  
_Change into your project folder_ and run the following command:

    git rm -r --cached .idea

This removes (`rm`) recursively (`-r`) the `.idea` folder, but only from the
index, not the local disk (`--cached`).

# Practice & Extension Work

The final part of pracs will usually be for you to do outside prac time.  
Use these exercises as normal practice and as ways to learn new things.

## Practice

### Random Things

Write 3 different versions of code to generate a random Boolean (`True` or `False`).

### More Random Conrad

Replace the literal values for the constants at the top (like
`MAX_INCREASE`) with randomly generated values (within sensible ranges).

### ASCII Table

Computers use ASCII to define a character-encoding scheme for letters,
digits, and other characters. It is useful to become familiar with ASCII
since that is how string comparisons are made.

Mr. Black the school teacher wants an educational program for his school
students to explore the details of ASCII. He wants the app to allow a
student to input a character and see the corresponding ASCII code, and
vice versa. A sample run of the program should look like (where `g` and `100` are user inputs):

    Enter a character: g
    The ASCII code for g is 103
    Enter a number between 33 and 127: 100
    The character for 100 is d

1. Start new file, `ascii_table.py`, and write code for this program.
   Remember that you can use the ord() and chr() functions to convert
   characters to ASCII integer values and vice versa.

2. Add error checking so that the number entered must be between the
   LOWER (33) and UPPER (127) bounds. Use **constants** for these
   values and use them in both your print statement and in your while
   loop condition. **That is, the numbers 33 and 127 should appear only
   once**.  
   Use f-strings everywhere you print literals and variable values together.

3. Add on to this program by writing code that displays a table with
   two columns, one for the numeric ASCII value and the other for the
   character itself. Use string formatting to align the text
   nicely in two columns. Print the values between LOWER and UPPER.  
   It should output like ("..." indicates parts that have been removed to
   save space):

        33  !
        34  "
       ...
        99  c
       100  d
       ...

### Debugging

Open your **Capitalist Conrad** program.  
Let's step through the program using the interactive debugger now...

1. Add a **breakpoint** on the while line by clicking in the left
   margin:    
   ![Breakpoint](../images/03image7.png)

2. Click the "debug" button or choose Run > Debug from the menu or
   press Shift+F9  
   The program will run until it hits the breakpoint - then stop and
   show you the current state of the program and its variables (both
   in the bottom window and in your code)

3. Try all the different methods for stepping through the program
   using the toolbar:    
   ![Debugger toolbar](../images/03image8.png)

## Extension

### ASCII Columns Challenge

Add columns to your ASCII table output from the earlier questions. Ask the user for how many
columns to print, then figure out how to write loop(s) and print
statements to achieve this.

### Word Generator

The following program randomly generates words by constructing a string
from random combinations of characters. The word_format variable stores
a sequence like ccvc, which means: consonant consonant vowel consonant.
The `random.choice` function is a useful way to select a single value
from a sequence of values.

Notice how the variable `word` starts as an empty string and then is
constructed using repeated string concatenation (with the `+` operator).

Try this and see if you can get any interesting words.

Copy the code from [word_generator.py](word_generator.py)

Things To Do:

- Get the word format from the user so that they can customise it. Convert
  it to lowercase using a string method.

- Try and make the program more interesting. For example:

  a. Use wildcards for the vowels (#) and consonants (%) or either
  (*) and make alphabetical characters use that actual
  character - e.g. the format "%re#*l*" might produce a word
  like "greatly" or "breuzla"

  b. Automatically (randomly) generate the word_format variable.

### Automatic Password Generator

Write a program that asks for a length and what characteristics it
must have - requirements for upper/lower/numeric/special characters -
then it should generate a password that matches.  
Use your earlier program's checker functionality to validate the
generated password.

# Solutions to Selected Exercises

It is ***super important*** that you use any provided
solutions to **help you learn**, not to avoid learning!  
Do the work yourself first, and *only* check the solutions to evaluate your work - not to do it for you. **OK?**

Some solutions (not all) for practicals are provided in the
**solutions** branch of the Practicals repository on GitHub:
<https://github.com/CP1404/Practicals/tree/solutions>

# Deliverables

This section summarises the expectations for marking in this practical.  
Please follow the [submission guidelines](../README.md#submission) to ensure you receive marks for your work.

- Type the URL of your GitHub practicals repository in the text box when you submit your practical.
- `string_formatting.py`
- `randoms.py`
- `capitalist_conrad.py`
- `exceptions_demo.py`
- `exceptions_to_complete.py`
- `password_checker.py`
- `files.py`

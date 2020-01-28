# Practical 02 - Strings, Files, Exceptions

**Did you finish last week's work?** If not, make sure to complete it
during the week. If you do not understand anything, bring those
questions to your tutor at the start of the following week.

# Remarkably Important!

- **DO NOT make a new project for each practical!**   
- **Create a new folder called `prac_02`** in your existing practicals project.
- Remember that you just keep using the same PyCharm project for all practicals.  

This really does make a difference and will save lots of time and effort if you do it correctly to start with.  
Please don't use multiple projects as then you can't use version control properly (important for Git/GitHub in prac 3)  
Please don't use spaces in file or folder names as then they are invalid module names (important for importing in prac 6)    

# Walkthrough Example

## String Formatting

The **format()** string method lets us format strings using placeholders
and format specifiers in a way that's very powerful and will make a lot
of sense once you get used to it. Remember that a *method* is a function
that runs on a particular object, so a string method runs on a string
like: `"literal".format(...)` or `variable.upper()`  
Sometimes the best way to start learning this sort of thing is to see
some useful examples, so:

-   Create a new Python file called `string_formatting_examples.py` in
    your `prac_02` folder.

-   (Remember when copying code from GitHub to click **Raw** first so
    that the formatting copies properly.)  
    Copy the following string formatting examples from
    [string_formatting_examples.py](string_formatting_examples.py)
    into this file and run the code. (It's also written below for your
    reference.)

    ```python
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.4
    
    # The 'old' manual way to format text with string concatenation:
    print("My guitar: " + name + ", first made in " + str(year))
    
    # A better way - using str.format():
    print("My guitar: {}, first made in {}".format(name, year))
    print("My guitar: {0}, first made in {1}".format(name, year))
    print("My {0} was first made in {1} (that's right, {1}!)".format(name, year))
    
    # Formatting currency (grouping with comma, 2 decimal places):
    print("My {} would cost ${:,.2f}".format(name, cost))
    
    # Aligning columns:
    numbers = [1, 19, 123, 456, -25]
    for number in numbers:
        print("Number is {:>5}".format(number))
    
    # A version of the above loop using the enumerate function, useful when you want the index and value
    for i, number in enumerate(numbers):
        print("Number {0} is {1:>5}".format(i + 1, number))
    ```

***Nice!*** Notice:

-   You can leave out the positional arguments, that is the numbers
    inside the {}, if you just want to use the default order.

-   You can also repeat values by repeating the positional arguments.

-   And you can do lots of formatting by using the string formatting
    'mini language'; details come after the **:**  See: <https://docs.python.org/3/library/string.html#formatstrings>

**Tips for string formatting with the format specifier {}**

- The number *before* the colon, or if there's no colon like {0},
specifies which parameter to use. This can be left out to use the
default order.

- The part *after* the colon specifies the formatting. E.g. {:3} specifies
to use 3 spaces (or more if needed) for the value when it's used.

- By default, **numbers are right-aligned** and **strings are
left-aligned**. You can change this with > or <  
So, {:>6} would format the value to be right-aligned and take up 6 (or
more if needed) spaces.

### Things to do:

Use string formatting to produce the output:  
(Notice where the values go and also the float formatting / number of decimal places.)
```
1922 Gibson L-5 CES for about $16,035!
```

Using a **for** loop with the **range** function and **string
formatting** (do not use a list), produce the following output (right-aligned numbers):

      0
     50
    100
    150

## Random Numbers

We are going to write some programs using random numbers... but how do
we generate random numbers? Python has a number of random functions -
contained within the **random** module. Unlike the built-in functions
(**print()**, **input()**, etc) the random functions are *not* built-in
but need to be **imported**. Modules are reusable collections of
functions, classes and variables (constants) related to a specific topic
(e.g. maths, operating system services, handling dates and times).
Python has a useful built-in function for finding out about the local
scope of something, called **dir()**.

**Launch a Python console** (in PyCharm, simply click in the
footer/status bar where it says "Python Console") and type the following 
at the `>>>` prompt:

    dir(str)
    
This will give you a display of the "dictionary" of everything contained in `str`, like:

    ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

Look carefully! You can see all of those useful **str** methods such as
**upper()**, **startswith()**, **isdecimal()**.

Next try running the **dir()** function with **random** as the argument:

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

This shows you all of the names in the module - most of which are
functions you can use. To use functions from a module that's been
imported like this you need to *qualify* the name - e.g. use
**random.randint** not just **randint**. Use **help()** to find out
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


Note: the name of a function can be used without the brackets here, but this
does not execute the function.

### Try This Out
`randoms.py` (Note: never name a file the same as a module; 
e.g. `random.py` or it will have higher precedence when you, e.g. `import random`)  

In your **console**, type in the following (run each print line multiple
times), and write the answers to the questions below in comments in `randoms.py`.

```python
import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3
```

-   *What did you see on line 1?*  
    What was the smallest number you could have seen, what was the
    largest?

-   *What did you see on line 2?*  
    What was the smallest number you could have seen, what was the
    largest?  
    *Could line 2 have produced a 4?*

-   *What did you see on line 3?*  
    What was the smallest number you could have seen, what was the
    largest?

-   Write code, not a comment, to produce a random number between 1 and 100 inclusive.

## Example to Study

This example combines some of the control structures (while loops, if
statements) from last week with some useful string formatting for
displaying currency.

Capitalist Conrad wants us to write a stock-price simulator for a
volatile stock. The price starts off at $10.00, and, at the end of
every day there is a 50% chance it increases by 0 to 10%, and a 50%
chance that it decreases by 0 to 5%. If the price rises above $1000, or
falls below $0.01, the program should end. The price should be
displayed to the nearest cent (e.g. $33.59, not $33.5918232901).

**What module do we need to import?** random

**What functions from random do we need to use?** randint (for the 50%
chance of increase or decrease), and uniform (to generate a random
floating-point number)

Download the code from: [capitalist_conrad.py](capitalist_conrad.py)


### Things To Do:

1.  The program currently runs without telling us how many days it
    simulated.  
    Add this feature using a day counter and string formatting so that
    the program prints like:

        Starting price: $10.00  
        On day 1 price is: $9.89  
        ...  
        On day 424 price is: $915.71  
        On day 425 price is: $1,001.60  

2.  Notice how the use of CONSTANTS makes the program easier to read and
    customise.  
    Try changing these so the allowed price range is $1 to $100 and
    the increase could be up to 17.5% (remember to change any comments
    that refer to constant values)  
    Run the program with these new values.

3.  Update your program so that it prints (writes) the output to a
    **file**.  
    How do we do this?

    -   First you need to **open** the file for writing. You only need
        to do this once, so add this line before your loop starts:

        `out_file = open(OUTPUT_FILE, 'w')`
    
        Note that this code line expects you to define the constant
        OUTPUT_FILE, so do that above.

    -   Update any print statements, so they output to the file.  
        Here's an (incomplete) example:
    
        `print("${:,.2f}".format(price), file=out_file)`
    
    -   **Close** the file at the very end:
    
        `out_file.close()`

*Keep going... :)*

## Exceptions

Copy this example code that uses exceptions: [exceptions_demo.py](exceptions_demo.py)
(also shown below), and run it, then answer the questions below in comments...

```python
try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
```

**Questions**

1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?

If you could figure out the answer to question 3, then **make this
change now**.

# Intermediate Exercises

## Problem For You To Fill In The Blanks - Exceptions

Let's write a program that gets an integer from the user and does not
crash when a non-number is entered. Copy the code below and modify/add
the parts highlighted so that it works and prints the number at the end:
[exceptions_to_complete.py](exceptions_to_complete.py)

```python
finished = False
result = 0
while not finished:
    try:
        # TODO: this line
        # TODO: this line
        pass
    except:  # TODO - add something after except
        print("Please enter a valid integer.")
print("Valid result is:", result)
```

Remove `pass` when you're finished.  
It's only there to prevent a syntax error.

*You're doing well. Keep it up...*

# Do-from-scratch Exercises

## Files

The solutions for these programs are provided, to
help you get going - or to confirm that your solution was valid.    
Note: when you execute a Python program that contains a line like
`open('data.txt', 'w')` the new file "data.txt" is created in the
same folder as the Python file in your PyCharm project.

Create a new file called **files.py** and do all of the following *separate questions* in it:  
Note: the intention is to give you experience using different ways to read files.  
Make sure you're confident with:

- `read()`
- `readline()`
- `readlines()`
- `for line in file`

1.  Write code that asks the user for their name, then opens a file
    called "name.txt" and writes that name to it.

2.  Write code that opens "name.txt" and reads the name (as above)
    then prints,  
    "Your name is Bob" (or whatever the name is in the file).

3.  Create a text file called `numbers.txt` and save it in your `prac_02`
    directory. Put the following three numbers on separate lines in the file
    and save it:  
    17  
    42  
    400  
    Write code that opens "numbers.txt", reads only the first two numbers and adds
    them together then prints the result, which should be... 59.

4.  Now write a fourth block of code that prints the total for all lines in `numbers.txt`
    or a file with *any* number of numbers.

## Password Checker

Download the starter code (complete with hints in the form of #TODO
comments) from [password_checker.py](password_checker.py)

Write a program that asks for and validates a person's password. The
program is not for comparing a password to a known password, but
validating the 'strength' of a new password, like you see on websites:
enter your password and then it tells you if it's valid (matches the
required pattern) and re-prompts if it's not.  
All passwords must contain *at least one each of: number*, *lowercase*
and *uppercase* character.  
  
The starter code uses constants (variables at the top of the code, named
in ALL_CAPS) to store:

a.  the minimum and maximum length of the password

b.  whether or not a special character (not alphabetical or numerical)
    is required

Remember when a program has CONSTANTS, you should use them everywhere you can so that if you change them at the top, this change affects the whole program as expected.  
E.g. if you changed the minimum length to 5, the program should print 5 and should check to make sure the password is >= 5 characters long.

Output should look something like this:

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

**Important Note:** Do not just try and Google "Python password checker"
or something, but think about doing this step by step. We have started
this for you with TODO comments in the code provided.

-   First, just check if a string has at least one lowercase character.  
    You can do this by looping through the string (for character in
    password:) and testing each character... count the ones that match
    (using **character.islower()**)... At the end you know how many
    lowercase characters there are.

-   Only when you are able to count lowercase, then, in the same loop,
    count the uppercase characters  
    That is, **do not** try and get all of the checks working before you
    know the first one works. **Do** one at a time.

-   *Then*, count the numbers...  
    Test your code for each of these changes as you write them

-   For special characters, remember you can use the **in** operator to
    see if the character is **in** another string (like a constant called
    SPECIAL_CHARACTERS)

-   ... keep going until you can tell how many of each kind of character
    there are

-   Then put it all together and test with some different settings.

**We hope this incremental approach makes sense and that you use it for
everything you code.**

When you have the program working, replace the inconsistent printing of
text and variables with nice string formatting using the `str.format()`
method.

## Got your GitHub on?

If you haven't setup your own GitHub account, please do so now. See our
instructions at:
<https://github.com/CP1404/Starter/wiki/Software-Setup#github>

Note that you should use a meaningful username that identifies who you
are and you must use your JCU email address. (If you already have a
GitHub account with a non-JCU address, you can add your JCU email as a
secondary email; you do not need to create a new account.)  
Ideally, JCU staff should be able to tell who you are from your
username. Your GitHub account is an important and professional record of
your work. You will likely use it as an online portfolio in the future.

# Practice & Extension Work

The final part of pracs will usually be for you to do outside of prac
time.  
Use these exercises as normal practice and as ways to learn new things.

##Practice

**Random Things**
Write 3 different versions of code to generate a random Boolean (True or False).  

**More Random Conrad**

Replace the literal values for the constants at the top (like
MAX_INCREASE) with randomly generated values (within sensible ranges)

### ASCII Table

Computers use ASCII to define a character-encoding scheme for letters,
digits, and other characters. It is useful to become familiar with ASCII
since that is how string comparisons are made.

Mr. Black the school teacher wants an educational program for his school
students to explore the details of ASCII. He wants the app to allow a
student to input a character and see the corresponding ASCII code, and
vice versa. A sample run of the program should look like (where **g** and
**100** are user inputs):

    Enter a character: g
    The ASCII code for g is 103
    Enter a number between 33 and 127: 100
    The character for 100 is d

1.  Start new file, `ascii_table.py`, and write code for this program.
    Remember that you can use the ord() and chr() functions to convert
    characters to ASCII integer values and vice versa.

2.  Add error checking so that the number entered must be between the
    LOWER (33) and UPPER (127) bounds. Use **constants** for these
    values and use them in both your print statement and in your while
    loop condition. **That is, the numbers 33 and 127 should appear only
    once**.  
    Use the **str.format()** method everywhere you print literals and
    variable values.

3.  Add on to this program by writing code that displays a table with
    two columns, one for the numeric ASCII value and the other for the
    character itself. Use the string **format()** method to align the text
    nicely in two columns. Print the values between LOWER and UPPER.  
    It should output like ("..." indicates parts that have been removed to
    save space):

         33  !
         34  "
        ...
         99  c
        100  d
        ...

## Extension

**ASCII Columns Challenge** 

Add columns to your ASCII table output from the earlier questions. Ask the user for how many
columns to print, then figure out how to write loop(s) and print
statements to achieve this.

**Word Generator**

The following program randomly generates words by constructing a string
from random combinations of characters. The word_format variable stores
a sequence like ccvc, which means: consonant consonant vowel consonant.
The **random.choice** function is a useful way to select a single value
from a sequence of values.

Notice how the variable `word` starts as an empty string and then is
constructed using repeated string concatenation (with the `+` operator).

Try this and see if you can get any interesting words.

Copy the code from [word_generator.py](word_generator.py)

Things To Do:

-   Get the word format from the user so they can customise it. Convert
    it to lowercase using a str method.

-   Try and make the program more interesting. For example:

    a.  Use wildcards for the vowels (#) and consonants (%) or either
        (*) and make alphabetical characters use that actual
        character - e.g. the format "%re#*l*" might produce a word
        like "greatly" or "breuzla"

    b.  Automatically (randomly) generate the word_format variable.

**Automatic Password Generator**

Write a program that asks for a length and what characteristics it
must have - requirements for upper/lower/numeric/special characters -
then it should generate a password that matches.  
Use your earlier program's checker functionality to validate the
generated password.

# Solutions to Selected Exercises

**Note:** it is ***super important*** that you use any provided
solutions to **help you learn**, not to avoid learning!  
Do the work yourself first, and *only* check the solutions to evaluate
your own work - not to do it for you. **OK?**

Some solutions (not all) for practicals will be provided in the
**solutions** branch of the Practicals repository on GitHub:
<https://github.com/CP1404/Practicals/tree/solutions>


# Deliverables
This section summarises the expectations for marking in this practical.

- string_formatting_examples.py
- randoms.py
- capitalist_conrad.py
- exceptions_demo.py
- exceptions_to_complete.py
- files.py
- password_checker.py
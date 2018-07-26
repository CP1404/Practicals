# Practical 02 - Strings, Files, Exceptions

**Did you finish last week's work?** If not, make sure to complete it
during the week. If you do not understand anything, bring those
questions to your tutor at the start of the following week.

# Walkthrough Example

## String Formatting


The **format()** string method lets us format strings using placeholders
and format specifiers in a way that's very powerful and will make a lot
of sense once you get used to it. Remember that a *method* is a function
that runs on a particular object, so a string method runs on a string
like: \"literal\".format(...) or variable.upper()  
Sometimes the best way to start learning this sort of thing is to see
some useful examples, so:

-   (Remember that you just keep using the same PyCharm project for all
    practicals, you don\'t need to make a new one for each prac.)  
    Create a new folder called prac\_02 in your practicals project

-   Create a new Python file called string\_formatting\_examples.py in
    this folder.

-   (Remember when copying code from GitHub to click **Raw** first so
    that the formatting copies properly.)  
    Copy the following string formatting examples from
    <https://github.com/CP1404/Practicals/blob/master/prac_02/string_formatting_examples.py>
    into this file and run the code. It\'s also written below for your
    reference (but copying from PDFs doesn\'t work well).

        name = **\"Gibson L-5 CES\"**

        year = 1922

        cost = 16035.40

\# The 'old' manual way to format text:

    print(**\"My guitar: \"** + name + **\", first made in \"** + str(year))

\# A better way - using str.format():

print(**\"My guitar: {}, first made in {}\"**.format(name, year))

print(**\"My guitar: {0}, first made in {1}\"**.format(name, year))

print(**\"My {0} was first made in {1} (that\'s right,
{1}!)\"**.format(name, year))  
  
\# Formatting currency:

print(**\"My {} would cost \${:,.2f}\"**.format(name, cost))

\# Aligning columns:

numbers = \[1, 19, 123, 456, -25\]

**for** i **in** range(len(numbers)):

print(**\"Number {0} is {1:\>5}\"**.format(i + 1, numbers\[i\]))

***Nice!*** Notice:

-   You can leave out the positional arguments, that is the numbers
    inside the {}, if you just want to use the default order.

-   You can also repeat values by repeating the positional arguments.

-   And you can do lots of formatting by using the string formatting
    'mini language'; details come after the **:**

Want to read more about it?
<https://docs.python.org/3/library/string.html#formatstrings> [
]{.underline}

### Things to do:

Using a **for** loop with the **range** function and **string
formatting**, produce the following output (right-aligned numbers):

0

50

100

**Tips for string formatting with the format specifier {}**

The number *before* the colon, or if there\'s no colon like {0},
specifies which parameter to use. This can be left out to use the
default order.

The part *after* the colon specifies the formatting. E.g. {:3} specifies
to use 3 spaces (or more if needed) for the value when it\'s used.

By default, **numbers are right-aligned** and **strings are
left-aligned**. You can change this with \> or \<  
So, {:\>6} would format the value to be right-aligned and take up 6 (or
more if needed) spaces.

Random Numbers
--------------

We are going to write some programs using random numbers... but how do
we generate random numbers? Python has a number of random functions -
contained within the **random** module. Unlike the built-in functions
(**print()**, **input()**, etc) the random functions are *not* built-in
but need to be **imported**. Modules are reusable collections of
functions, classes and variables (constants) related to a specific topic
(e.g. maths, operating system services, handling dates and times).
Python has a useful built-in function for finding out about the local
scope of something, called **dir()**.

Launch a Python **console** (in PyCharm, simply click in the
footer/status bar where it says "Python Console") and try the following:

\>\>\> **dir(str)**

\[\'\_\_add\_\_\', \'\_\_class\_\_\', \'\_\_contains\_\_\',
\'\_\_delattr\_\_\', \'\_\_dir\_\_\', \'\_\_doc\_\_\', \'\_\_eq\_\_\',  
... \'isnumeric\', \'isprintable\', \'isspace\', \'istitle\',
\'isupper\', \'join\'...\]

Look carefully! You can see all of those useful **str** methods such as
**upper()**, **startswith()**, **isdecimal()**.

Next try running the **dir()** function with **random** as the argument:

\>\>\> **dir(random)**

Traceback (most recent call last):

File \"\<input\>\", line 1, in \<module\>

NameError: name \'random\' is not defined

This doesn't work, since random is a **module** that needs to be
**imported**.

Now try it like this:

\>\>\> **import random**

\>\>\> **dir(random)**

\[\'BPF\', \'LOG4\', \'NV\_MAGICCONST\', \'RECIP\_BPF\', \'Random\',
\'SG\_MAGICCONST\', \'SystemRandom\', ... \'randint\', \'random\',
\'randrange\', \'sample\', \'seed\', \'setstate\', \'shuffle\',
\'triangular\', \'uniform\', \'vonmisesvariate\', \'weibullvariate\'\]

This shows you all of the names in the module - most of which are
functions you can use. To use functions from a module that's been
imported like this you need to *qualify* the name - e.g. use
**random.randint** not just **randint**. Use **help()** to find out
about a couple of these functions:

\>\>\> **help(random.randint)**

Help on method randint in module random:

randint(a, b) method of random.Random instance

Return random integer in range \[a, b\], including both end points.

\>\>\> **help(random.randrange)**

Help on method randrange in module random:

randrange(start, stop=None, step=1, \_int=\<class \'int\'\>) method of
random.Random instance

Choose a random item from range(start, stop\[, step\]).

This fixes the problem with randint() which includes the

endpoint; in Python this is usually not what you want.

Note: the name of a function can be used without the brackets, but this
does not execute the function!

### Try This Out

In your **console**, type in the following (run each print line multiple
times), and answer the questions below.

import random

print(random.randint(5, 20)) \# line 1

print(random.randrange(3, 10, 2)) \# line 2

print(random.uniform(2.5, 5.5)) \# line 3

-   *What did you see on line 1?  
    What was the smallest number you could have seen, what was the
    largest?*

-   *What did you see on line 2?  
    What was the smallest number you could have seen, what was the
    largest?  
    Could line 2 have produced a 4?*

-   *What did you see on line 3?  
    What was the smallest number you could have seen, what was the
    largest? *

Example to Study
----------------

This example combines some of the control structures (while loops, if
statements) from last week with some useful string formatting for
displaying currency.

Capitalist Conrad wants us to write a stock-price simulator for a
volatile stock. The price starts off at \$10.00, and, at the end of
every day there is a 50% chance it increases by 0 to 10%, and a 50%
chance that it decreases by 0 to 5%. If the price rises above \$1000, or
falls below \$0.01, the program should end. The price should be
displayed to the nearest cent (e.g. \$33.59, not \$33.5918232901).

**What module do we need to import?** random

**What functions from random do we need to use?** randint (for the 50%
chance of increase or decrease), and uniform (to generate a random
floating-point number)

Download the code from:
<https://github.com/CP1404/Practicals/blob/master/prac_02/capitalist_conrad.py>

import random  
MAX\_INCREASE = 0.1 *\# 10%  
*MAX\_DECREASE = 0.05 *\# 5%  
*MIN\_PRICE = 0.01  
MAX\_PRICE = 1000.0  
INITIAL\_PRICE = 10.0  
  
price = INITIAL\_PRICE  
print(**\"\${:,.2f}\"**.format(price))  
  
**while** price \>= MIN\_PRICE **and** price \<= MAX\_PRICE:  
price\_change = 0  
*\# generate a random integer of 1 or 2  
\# if it\'s 1, the price increases, otherwise it decreases  
***if** random.randint(1, 2) == 1:  
*\# generate a random floating-point number  
\# between 0 and MAX\_INCREASE  
*price\_change = random.uniform(0, MAX\_INCREASE)  
**else**:  
*\# generate a random floating-point number  
\# between negative MAX\_DECREASE and 0  
*price\_change = random.uniform(-MAX\_DECREASE, 0)  
  
price \*= (1 + price\_change)  
print(**\"\${:,.2f}\"**.format(price))

### Things To Do:

1.  The program currently runs without telling us how many days it
    simulated.  
    Add this feature using a day counter and string formatting so that
    the program prints like:

> Starting price: \$10.00
>
> On day 1 price is: \$9.89
>
> ...
>
> On day 424 price is: \$915.71
>
> On day 425 price is: \$1,001.60

2.  Notice how the use of CONSTANTS makes the program easier to read and
    customise.  
    Try changing these so the allowed price range is \$1 to \$100 and
    the increase could be up to 17.5% (remember to change any comments
    that refer to constant values)  
    Run the program with these new values.

3.  Update your program so that it prints (writes) the output to a
    **file**. How do we do this?

    -   First you need to **open** the file for writing. You only need
        > to do this once, so add this line before your loop starts:

> out\_file = open(OUTPUT\_FILE, **\'w\'**)
>
> Note that this code line expects you to define the constant
> OUTPUT\_FILE, so do that above.

-   Update any print statements, so they output to the file -
    > (incomplete) example:

> print(**\"\${:,.2f}\"**.format(price), file=out\_file)

-   **Close** the file at the very end:

> out\_file.close()

*Keep going... :)  
*

Exceptions
----------

Here is some example code that uses exceptions.

Copy the code from
<https://github.com/CP1404/Practicals/blob/master/prac_02/exceptions_demo.py>

(also shown below), and run it, then answer the questions below...

> **try**:
>
> numerator = int(input(**\"Enter the numerator: \"**))
>
> denominator = int(input(**\"Enter the denominator: \"**))
>
> fraction = numerator / denominator
>
> print(fraction)
>
> **except** ValueError:
>
> print(**\"Numerator and denominator must be valid numbers!\"**)
>
> **except** ZeroDivisionError:
>
> print(**\"Cannot divide by zero!\"**)
>
> print(**\"Finished.\"**)

**Questions**

> 1\. When will a ValueError occur?
>
> 2\. When will a ZeroDivisionError occur?
>
> 3\. Could you change the code to avoid the possibility of a
> ZeroDivisionError?

If you could figure out the answer to question 3, then **make this
change now**.

Intermediate Exercises
======================

Problem For You To Fill In The Blanks - Exceptions
--------------------------------------------------

Let's write a program that gets an integer from the user and does not
crash when a non-number is entered. Copy the code below and modify/add
the parts highlighted so that it works and prints the number at the end:
<https://github.com/CP1404/Practicals/blob/master/prac_02/exceptions_to_complete.py>

> finished = False
>
> result = 0
>
> while not finished:
>
> try:
>
> \_\_\_\_\_\_\_
>
> \_\_\_\_\_\_\_
>
> except \_\_\_\_\_\_\_:
>
> print(\"Please enter a valid integer.\")
>
> print(\"Valid result is:\", result)

*You\'re doing well. Keep it up...*

Do-from-scratch Exercises
=========================

Files
-----

The solutions for these programs are at the bottom of the practical, to
help you get going - or to confirm that your solution was valid.  
Note: when you execute a Python program that contains a line like
**open(\'data.txt\', \'w\')** the new file "data.txt" is created in the
same folder as the Python file in your PyCharm project.

Do all of the following in a single file called **files.py**:

1.  Write a program that asks the user for their name, then opens a file
    called "name.txt" and writes that name to it.

2.  Write a program that opens "name.txt" and reads the name (as above)
    then prints,  
    "Your name is Bob" (or whatever the name is in the file).

3.  Create a text file called "numbers.txt" (You can create a simple
    text file in PyCharm with Ctrl+N, choose "File" and save it in your
    project). Put the numbers 17 and 42 on separate lines in the file
    and save it:  
    17  
    42  
    Write a program that opens "numbers.txt", reads the numbers and adds
    them together then prints the result, which should be... 59.

4.  **Extended** (perhaps only do this if you're cruising... if you are
    struggling, just read the solution) ...  
    Now extend your program so that it can print the total for a file
    containing *any* number of numbers.

Password Checker
----------------

Download the starter code (complete with hints in the form of \#TODO
comments) from:
<https://github.com/CP1404/Practicals/blob/master/prac_02/password_checker.py>

Write a program that asks for and validates a person's password. The
program is not for comparing a password to a known password, but
validating the \'strength\' of a new password, like you see on websites:
enter your password and then it tells you if it's valid (matches the
required pattern) and re-prompts if it's not.  
All passwords must contain *at least one each of: number*, *lowercase*
and *uppercase* character.  
  
The starter code uses constants (variables at the top of the code, named
in ALL\_CAPS) to store:

a.  the minimum and maximum length of the password

b.  whether or not a special character (not alphabetical or numerical)
    is required

When a valid password is entered, it should print it on the screen along
with its length.

Output should look something like this:

> Please enter a valid password
>
> Your password must be between 5 and 15 characters, and contain:
>
> 1 or more uppercase characters
>
> 1 or more lowercase characters
>
> 1 or more numbers
>
> and 1 or more special characters:
> !@\#\$%\^&\*()\_-=+\`\~,./\'\[\]\<\>?{}\|  
>
> \> this?
>
> Invalid password!
>
> \> whyNot?CanIhaveThis?
>
> Invalid password!
>
> \> 12345678901234567890aBcv@
>
> Invalid password!
>
> \> thisISmy123Pass!
>
> Invalid password!
>
> \> 1thisISit!
>
> Your 10 character password is valid: 1thisISit!

Here's another run with the same code but different values for the
constants (special characters are not required in this version):

> Please enter a valid password
>
> Your password must be between 2 and 6 characters, and contain:
>
> 1 or more uppercase characters
>
> 1 or more lowercase characters
>
> 1 or more numbers
>
> \> aB
>
> Invalid password!
>
> \> HowCanIHave2Chars?
>
> Invalid password!
>
> \> 1aB
>
> Your 3 character password is valid: 1aB

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
    see if the character is in another string (like a constant called
    SPECIAL\_CHARACTERS)

-   ... keep going until you can tell how many of each kind of character
    there are

-   Then put it all together and test with some different settings.

**We hope this incremental approach makes sense and that you use it for
everything you code.**

When you have the program working, replace the inconsistent printing of
text and variables with nice string formatting using the str.format()
method.

Got your GitHub on?
-------------------

If you haven\'t setup your own GitHub account, please do so now. See our
instructions at:
<https://github.com/CP1404/Starter/wiki/Software-Setup#github>

Note that you should use a meaningful username that identifies who you
are and you must use your JCU email address. (If you already have a
GitHub account with a non-JCU address, you can add your JCU email as a
secondary email; you do not need to create a new account.)  
Ideally, JCU staff should be able to tell who you are from your
username. Your GitHub account is an important and professional record of
your work. You will likely use it as an online portfolio in the future.

Practice & Extension Work
=========================

The final part of pracs will usually be for you to do outside of prac
time.  
Use these exercises as normal practice and as ways to learn new things.

ASCII Table
-----------

Computers use ASCII to define a character-encoding scheme for letters,
digits, and other characters. It is useful to become familiar with ASCII
since that is how string comparisons are made.

Mr. Black the school teacher wants an educational program for his school
students to explore the details of ASCII. He wants the app to allow a
student to input a character and see the corresponding ASCII code, and
vice versa. The output of the program should look like (where **g** and
**100** are user inputs):

Enter a character: **g**

The ASCII code for g is 103

Enter a number between 33 and 127: **100**

The character for 100 is d

1.  Start new file, ascii\_table.py, and write code for this program.
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
    character itself. Use the **str.format()** method to align the text
    nicely in two columns. Print the values between LOWER and UPPER.  
    It should output like (... shows parts that have been removed to
    save space):

33 !

34 \"

...

99 c

100 d

...

ASCII Columns Challenge 
------------------------

Add columns to your ASCII table output. Ask the user for how many
columns to print, then figure out how to write loop(s) and print
statements to achieve this.

Word Generator
--------------

The following program randomly generates words by constructing a string
from random combinations of characters. The word\_format variable stores
a sequence like ccvc, which means: consonant consonant vowel consonant.
The **random.choice** function is a useful way to select a single value
from a sequence of values.

Notice how the variable word starts as an empty string and then is
constructed using repeated string concatenation (with the + operator).

Try this and see if you can get any interesting words:

Copy the code below from:
<https://github.com/CP1404/Practicals/blob/master/prac_02/word_generator.py>

> **import** random
>
> VOWELS = **\"aeiou\"**
>
> CONSONANTS = **\"bcdfghjklmnpqrstvwxyz\"**
>
> word\_format = **\"ccvc\"**
>
> word = **\"\"**
>
> **for** kind **in** word\_format:
>
> **if** kind == **\"c\"**:
>
> word += random.choice(CONSONANTS)
>
> **else**:
>
> word += random.choice(VOWELS)
>
> print(word)

### Things To Do:

-   Get the word format from the user so they can customise it. Convert
    it to lowercase using a str method.

-   Try and make the program more interesting, For example:

    a.  Use wildcards for the vowels (\#) and consonants (%) or either
        (\*) and make alphabetical characters use that actual
        character - e.g. the format "%re\#\*l\*" might produce a word
        like "greatly" or "breuzla"

    b.  Automatically (randomly) generate the word\_format variable.

Automatic Password Generator
----------------------------

Write a program that should ask for a length and what characteristics it
must have - requirements for upper/lower/numeric/special characters -
then it should generate a password that matches.  
Use your earlier program's checker functionality to validate the
generated password.

More Random Conrad
------------------

Replace the literal values for the constants at the top (like
MAX\_INCREASE) with randomly generated values (that make sense)

Solutions to Selected Exercises
===============================

**Note:** it is ***super important*** that you use any provided
solutions to help you **learn**, not to avoid learning!  
Do the work yourself first, and *only* check the solutions to evaluate
your own work - not to do it for you. **OK?**

Some solutions (not all) for practicals will be provided in the
**solutions** branch of the Practicals repository on GitHub:
<https://github.com/CP1404/Practicals/tree/solutions>

Here also are some solutions to the quick file exercises...

> 1\. Write a program that asks the user for their name, then opens a file
> called "name.txt" and writes that name to it.
>
> 2\. Write a program that opens "name.txt" and reads the name (as above)
> then prints,
>
> "Your name is Bob" (or whatever the name is in the file).
>
> 3\. First, create a text file called "numbers.txt".
>
> Put the numbers 17 and 42 on separate lines in the file and save it.
>
> Write a program that opens "numbers.txt", reads the numbers and adds
> them together then prints the result, which should be... 59.
>
> *\# Quick Program 1*
>
> out\_file = open(**\"name.txt\"**, **\"w\"**)
>
> name = input(**\"What is your name? \"**)
>
> print(name, file=out\_file) \# or outFile.write(name)
>
> out\_file.close()
>
> *\# Quick Program 2*
>
> in\_file = open(**\"name.txt\"**, **\"r\"**)
>
> name = in\_file.read().strip()
>
> print(**\"Your name is\"**, name)
>
> in\_file.close()
>
> *\# Quick Program 3*
>
> *\# Note that .strip() is unnecessary since int() handles that
> whitespace*
>
> in\_file = open(**\"numbers.txt\"**, **\"r\"**)
>
> number1 = int(in\_file.readline())
>
> number2 = int(in\_file.readline())
>
> print(number1 + number2)
>
> in\_file.close()
>
> *\# Quick Program 3 extended - sum of all numbers*
>
> in\_file = open(**\"numbers.txt\"**, **\"r\"**)
>
> total = 0
>
> **for** line **in** in\_file:
>
> number = int(line)
>
> total += number
>
> print(total)
>
> in\_file.close()
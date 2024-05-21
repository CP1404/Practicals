# Practical 06 - Classes

## Code reviews help you learn!

Each practical from now on, you will do your work in a **new branch**, then do a **pull request**, mentioning a
new/different student to get (and give)
a code review.

[Find the right student to mention here each week (different for each practical)](https://github.com/CP1404/Starter/wiki/Code-Review-Order#prac-6)

So, every week, ***before*** starting the prac, ensure that your `master` branch is up-to-date, then create a new
branch.

You must **merge** your feedback branch on GitHub, then **pull** to update your local master branch.  
Then, ensure you are on the `master` branch, not the feedback branch.  
Then create a new branch, `prac_06_feedback`.  
See how this works?  
If you're not sure, please ask for help.

Expectations and marking for this prac include **doing a code review** not just requesting one.  
See the [submission deliverables](#deliverables) below.

## Classes

We have seen how to work with lists, tuples and dictionaries to store and process data appropriate for those types:

- `list` is useful for storing an ordered sequence of data (e.g., monthly rainfall data)
- `tuple` is useful for storing fixed (not changing) data with multiple parts (e.g., date of birth)
- `dict` is useful when the data has a 'mapping' relationship (e.g., name -> date of birth)

Very often we want to combine data into one object in a way that does not suit one of the built-in types, so we write
our own **classes** for these situations. That's what this practical is all about. As you do the prac, pay attention to
how the class construct helps us combine data and functions in one entity. Ask questions as needed!

# Walkthrough Example

First, please confirm that you are on an up-to-date feedback branch with all your previous work. OK?

Get (remember to click Raw)
[car.py](car.py) and [used_cars.py](used_cars.py) and add them to your PyCharm project in this week's prac folder.

The `import` statement assumes you have your `car.py` file in a folder called `prac_06` as we suggested.

Run your program and it should work.

**Spend some time studying the Car class.**

## Modifications

In the used_cars program file, write one new line of code for each of the following:

1. Create a new Car object called "limo" that is initialised with 100 units of fuel.

2. Add 20 more units of fuel to this new car object using the `add` method.

3. Print the amount of fuel in the car.

4. Attempt to drive the car 115 km using the `drive` method.

5. Now add the `__str__` method to the Car class in `car.py`.  
   Using f-string formatting. Make it return a string in the following format:    
   `Car, fuel=42, odometer=277`  
   Remember that you can run this method by **print**ing your car object, or passing the car object to the `str()`
   function.  
   **Do NOT** call the method verbosely like `my_car.__str__()`

6. Now add a `name` field to the Car class (in `car.py`), and adjust the `__init__` and `__str__` methods to set and
   display this respectively. Make the str method return the car's name instead of just "Car".  
   Now **add names** (literals) to the constructors where you create Car objects in the `used_cars.py` program.  
   Test your work and make sure you can now make and view named cars.

7. In your `used_cars.py` program, print your car object/s to make sure that the
   `__str__` method is working as expected.

# Intermediate Exercises

For each of the remaining exercises (as we've done before), read the question, then put an estimate of how long it will
take you in the module docstring.  
Record the current time here in your comment.  
When you've finished, check the time and record how long it actually took you.

File: `programming_language.py`
File: `languages.py`

Let's make our own simple class for a **programming language** in the file
`programming_language.py`

> [!NOTE]
> Remember that file/module names are always the same as the class but in lower case,
> with optional `_` for readability.

Follow Python's recommended "CapWords" style and call your class `ProgrammingLanguage`.

For each language, we want to store the following fields - the row names from this table,
based mostly on the information found at
[this Programming Language Comparison](http://www.jvoegele.com/software/langcomp.html) page.

| (Field)          | **Java** | **C++** | **Python** | **Visual Basic** | **Ruby** |
|------------------|----------|---------|------------|------------------|----------|
| ***Typing***     | Static   | Static  | Dynamic    | Static           | Dynamic  |
| ***Reflection*** | Yes      | No      | Yes        | No               | Yes      |
| ***Year***       | 1995     | 1983    | 1991       | 1991             | 1995     |

Define the following **methods**:

- `__init__` - like most init functions, create the fields and set them to the parameters passed in.

- `is_dynamic()` - which returns True/False if the programming language is dynamically typed or not.

> [IMPORTANT]
> Please understand that this function will take no parameters other than `self`.
> The data is already *inside* the object, so you don't need to tell the object its own data.

This function's purpose is to encapsulate the functionality that would make the class more helpful.  
See how the function name starts with `is`, like `isupper()`, `isnumeric()`, etc.?  
So, it returns a Boolean.

Create a simple program in `languages.py`

Import the class, then copy these lines into your new program:

```python
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)
```

Now add the `__str__` method to the class (not the client code), which should return a string like:

`Python, Dynamic Typing, Reflection=True, First appeared in 1991`

See if your `__str__` function is working properly by running the program to check that printing works as expected.

Now create a new list that contains these three existing `ProgrammingLanguage` objects.

![Pencil Icon](../images/pencil.png)

Do this next part on paper first, then copy it into PyCharm to see how you went.  
Remember that writing code on paper (or a whiteboard) can help you learn better (since you can't
depend on the IDE's help), and encourages you to be consistent and clear with syntax, indenting, etc.

Loop through and print the names of all the languages with dynamic typing (make sure you use your new `is_dynamic`
method!), which should produce output like:

    The dynamically typed languages are:
    Python
    Ruby

# Do-from-scratch Exercises

## Guitars!

File: `guitar.py`

Remember the string formatting example from prac 2:

```python
name = "Gibson L-5 CES"
year = 1922
cost = 16035.40
print(f"My guitar: {name}, first made in {year}")
```

You should notice that we have multiple values to store for one guitar entity:
name, year and cost... and that guitars are awesome! What if we owned 9 guitars? We'd want to use a collection like a
list... but what would each element in the list be? ... A tuple? A dictionary? No... This is a classic case for a class!

Write a `Guitar` class that allows you to store one guitar with these **fields** (attributes):

- `name`
- `year`
- `cost`

Define the following **methods**:

- `__init__` - with defaults `name="", year=0, cost=0`

- `__str__` - which uses {} string formatting to return something like (using the values from above):  
  `Gibson L-5 CES (1922) : $16,035.40`

- `get_age()` - which returns how old the guitar is in years (e.g., in 2022 the L-5 is: 2022 - 1922 = 100)

- `is_vintage()` - which returns `True` if the guitar is 50 or more years old, `False` otherwise  
  Hint: try using `get_age()` to simplify the implementation of this method!

Remember that methods should not take in any data that the object already knows (like age, year, etc.).

### Testing

File: `guitar_test.py`

Now write a program with at least enough code to test that the last two methods work as expected.  
To test `get_age()`, you could test that the above example guitar does indeed output 100 as
expected. Here's some sample output for testing two guitars where the second is called Another Guitar and has
year=2013:

    Gibson L-5 CES get_age() - Expected 100. Got 100
    Another Guitar get_age() - Expected 9. Got 9
    Gibson L-5 CES is_vintage() - Expected True. Got True
    Another Guitar is_vintage() - Expected False. Got False

Do you see how this works?

We print our own *literal* for what we expect if the function works (e.g., 100), then we print *what the method actually
returns*, and we look at the output to see if they match.  
This form of testing is quite 'manual' since we need to read the output and compare it ourselves, but it is a good
start.

Let's say we wrote the `is_vintage()` method incorrectly, then we **want** to see something like:

    50-year old guitar is_vintage() - Expected True. Got False

We can see that the actual does **not** match the expected, so we know we need to fix something.

### Playing the Guitars (not really)

File: `guitars.py`

Got your class working and tested? Great!   
Write a program that uses it.

This program should use a list to store all the user's guitars (keep inputting until they enter a blank name), then
print
their details.

> [!IMPORTANT]
> Read the full question including the notes *before* starting.  
> We've written helpful guidance to make this easier and to teach you valuable lessons.

**Sample Output** (**bold** is user entry):

<pre>
My guitars!
Name: <strong>Fender Stratocaster</strong>
Year: <strong>2014</strong>
Cost: $<strong>765.4</strong>
Fender Stratocaster (2014) : $765.40 added.

Name:

<em>... snip ...</em>

These are my guitars:
Guitar 1:       Gibson L-5 CES (1922), worth $ 16,035.40 (vintage)
Guitar 2:        Line 6 JTV-59 (2010), worth $  1,512.90
Guitar 3:  Fender Stratocaster (2014), worth $    765.40
</pre>

#### Programmer Efficiency Note

When testing a program like this you can waste a lot of time typing in input... then changing something, running it
again and... typing the same thing again...  
***So don't do it!***

Instead, comment out the user input lines, and put in lines like this to
'get' the data for testing:

```python
guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
```

According to Wikipedia's page on
the [abstraction principle](https://en.wikipedia.org/wiki/Abstraction_principle_(programming)):
> "When read as recommendation to the programmer, the abstraction
> principle can be generalised as the "[*don't repeat
> yourself*](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself)"
> principle, which recommends avoiding the duplication of information in
> general, and also avoiding the duplication of human effort involved in
> the software development process."

### Notes (you haven't started yet, have you?)

- The sample output uses some nice string formatting. Feel free to try and figure this out, or just use something like
  our code below (the width we use for
  `guitar.name` is just a guesstimate):

  ```python
  print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
  ```

  The variable `vintage_string` is set to `""` or `" (vintage)"`
  depending on the `is_vintage()` method.  
  If you're keen, try using Python's *ternary operator* to do this in one line.  
  E.g., to set the value of `category` to `adult` or `child` depending on `age`, you could use:

      category = "adult" if age >= 18 else "child"  

- For this particular code, we've used both `i` and the target variable
  `guitar` (instead of `guitars[i]`) by using the built-in
  **`enumerate()`** function.

  ```python
  for i, guitar in enumerate(guitars, 1):
      # do something with i (the index) and guitar (the element)
  ```

# Reflection

We are just past halfway, so it's helpful to stop and reflect, and adjust as needed.

Download and save the template markdown file [REFLECTION.md](REFLECTION.md) to your `prac_06` folder.  
Write short but meaningful answers to the questions in that file.

# Practice & Extension Work

Use these exercises as much-needed practice and as ways to learn new things.

## Practice

### Persons

Similar to the practice question with friends' names and addresses in prac 5,
create a program that uses a list of `Person` objects.  
Each `Person` object includes first-name, last-name and age.  
The user can type in the details of any number of people. The code generates a table formatted with the first-names,
last-names, and ages of the people (perhaps sort the people into order based on their ages).

### Driving Simulator

Create a car driving simulator in `car_simulator.py` that uses the `Car` class that works like the following sample
output...

> [!NOTE]
> Please do this (and every problem of significant size) incrementally:

- Start by just testing one method call,
- then another,
- then write the menu and put it all together.

Remember to use the class's functionality.  
Don't rewrite anything you've already got.

Do you remember how to construct a simple menu-driven program? If not, revise earlier
lectures and practicals.

You will need to `import` the `car` module, create a `Car` object, and use appropriate methods on that object.

    Let's drive!
    Enter your car name: The bomb
    The bomb, fuel=100, odo=0
    Menu:
    d) drive
    r) refuel
    q) quit
    Enter your choice: f
    Invalid choice
    
    The bomb, fuel=100, odo=0
    Menu:
    d) drive
    r) refuel
    q) quit
    Enter your choice: d
    How many km do you wish to drive? 39
    The car drove 39km.
    
    The bomb, fuel=61, odo=39
    Menu:
    d) drive
    r) refuel
    q) quit
    Enter your choice: d
    How many km do you wish to drive? -25
    Distance must be >= 0
    How many km do you wish to drive? 100
    The car drove 61km and ran out of fuel.
    
    The bomb, fuel=0, odo=100
    Menu:
    d) drive
    r) refuel
    q) quit
    Enter your choice: r
    How many units of fuel do you want to add to the car? -80
    Fuel amount must be >= 0
    How many units of fuel do you want to add to the car? 120
    Added 120 units of fuel.
    
    The bomb, fuel=120, odo=100
    Menu:
    d) drive
    r) refuel
    q) quit
    Enter your choice: d
    How many km do you wish to drive? 25
    The car drove 25km.
    
    The bomb, fuel=95, odo=125
    Menu:
    d) drive
    r) refuel
    q) quit
    Enter your choice: q
    
    Good bye The bomb's driver.

## Extension

### Date

> [!NOTE]
> Python has good modules for dates, like `date` and `datetime`.  
> You would usually use these, not write your own. This is a practice question.

Create a `Date` class, storing the fields:

- `day`
- `month`
- `year`

Write some useful methods, including:

- `__init__` and `__str__`
- `add_days(n)` - which should add n days to the stored date (perhaps harder than it seems)

Test the class.

![GitHub logo](../images/githublogo.png)

## Try using the command line for Git

It's a valuable skill! On the lab computers, you should be able to use **"Git Bash"**. Right-click on the folder where
your files are and select "Git Bash here".  
On a Mac, just use **Terminal**.

**Why?** Here's a quote from one of our students who completed this subject:
> "Now I'm moving into 2nd yr subjects, I found the integrated
> git/pycharm a good intro step, but I'm finding git bash with a simple
> cheat sheet is a nice progression. I think 99% of us could use some more
> training/practice with branching, merging, etc. Still kinda confusing in
> the terminology."

The more you have to do by yourself, the more you will really understand what's happening. Some things (like removing a
file from the index)
cannot be done with the IDE integration. So, as soon as you are happy to, start getting used to using git from a
console.

Create a new repo with `git init`, add some code, add files with `git add`, commit with `git commit`...

Then, next time you're ready to commit and push your practical work, try using the command line to do it!

# Deliverables

This section summarises the expectations for marking in this practical.  
Please follow the [submission guidelines](../README.md#submission) to ensure you receive marks for your work.

You may not receive your code review request in time to submit each week,
so we ask for the code review you did from the previous week.  
This week, please submit two PR URLs.

- Type the URL of your Pull Request (PR) that mentions another student **for this prac**.
- Type the URL of the PR that you reviewed **for the previous prac**.
- `car.py` modifications
- `used_cars.py` modifications (cars have names)
- `programming_language.py` (the class), `languages.py` (the client program)
- `guitar.py` (the class), `guitar_test.py` (the tests), `guitars.py` (the client program)
- `REFLECTION.md`
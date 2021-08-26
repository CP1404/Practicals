# Practical 08 - Inheritance

Don't forget to make a new branch (starting from `master`), `prac_08_feedback` _before_ you start!

In this practical, you will work on extending classes with inheritance.  
There's a lot of _teaching_ in this prac, so make sure you read carefully and do a lot of _learning!_

# Inheritance

We recently started making our own classes and objects:

- A **class** is a blueprint (the code) for creating an **object**
  (an object is also known as an **instance**).

- A class is a new **type**.

- **Objects** store data in instance variables (`self.something`) and provide access to the **methods** (functions)
  defined in the class.

Inheritance is (only) appropriate where you are building a more specialised version of a class. Inheritance can be
described as an "is a" relationship.  
When class Y inherits from class X, it should always be the case that an
**is a** relationship holds (Y "is a" X).

For example, a Tree is a Plant, but it's not true to say a Cat is a Dog. So, it is appropriate for a **Tree** class to
inherit from a **Plant**
class, but not appropriate for a **Cat** class to inherit from a **Dog**
class. Both Cat and Dog could inherit from **Animal**.

# Walkthrough Example

In a previous practical, we looked at a **Car** class. This time we will see that we can extend the Car class to make
a **Taxi** class, which is a more specialised version of a Car.

You can use your car from last week, or the finished version in the solutions. Either way, copy your `car.py` file to
your `prac_08` folder.

Download [taxi.py](https://github.com/CP1404/Practicals/blob/master/prac_08/taxi.py)

Read the code and note that the **Taxi** class *extends* the **Car**
class in two ways:

- it adds new attributes (**`price_per_km`**,
  **`current_fare_distance`**) and methods (**`get_fare`**,
  **`start_fare`**)

- it *overrides* methods (**`drive`**, **`__init__`** and
  **`__str__`**) to take account of the characteristics of a Taxi

Notice that the `drive` method still works the same way in terms of its ***interface*** - it takes in a distance
parameter, and it returns the distance driven. This is important for *polymorphism* - so we can treat all subclasses
of **Car** in the same way - we `drive()` a taxi the same way we `drive()` any other car.

## Test Taxi

File: `taxi_test.py`

Create a separate file to try out your taxi.  
Generally we don't write client code in class files, but rather we use separate files.

Write lines of code for each of the following (**hint**: use the methods available in the Taxi class):

1. Create a new taxi with name "Prius 1", 100 units of fuel and price of $1.23/km

2. Drive the taxi 40 km

3. Print the taxi's details and the current fare

4. Restart the meter (start a new fare) and then drive the car 100 km

5. Print the details and the current fare

## Class Variables

_Are you reading carefully and learning? Don't skim this!_

Depending on what kind of system you're modelling with **Taxi**, it might make sense that all taxis have the same price
per km. (We don't want to get into one taxi and pay $2.20, then find another one was only $1.20.) So, we can use a **
class variable**, which is a variable that is ***shared*** between all instances of that class. You define class
variables directly _after_ the class header line and _before_ any method definitions.

1. Add the **class variable** `price_per_km` to the Taxi class (in
   `taxi.py`) and set it to 1.23

2. Change the **`__init__`** function so that it does *not* take in the price_per_km, which means it doesn't need to set
   self.price_per_km because that's already set by the class variable.

   ```python
   class Taxi(Car):
       """Specialised version of a Car that includes fare costs."""
       price_per_km = 1.23
   
       def __init__(self, name, fuel):
           ...
   ```
3. Change any client code (where you create your Taxi objects)
   so that you don't pass in this value.

4. Test your code and see if you get the same output (you should).

   Note: when using class variables, you can either:

    - refer to the variable as `Taxi.price_per_km`, which explicitly refers to the class variable shared by any Taxi
      instances, or

    - use `self.price_per_km`, which refers to the instance variable that may or may not exist... Python looks for an
      instance variable in the object and if it doesn't find it there, then it looks up to the class variable, then it
      looks up to the parent class...  
      *This is usually preferred*, because it allows you to update the value for each object if needed (as we will see
      later with the SilverServiceTaxi).

# Intermediate Exercises

## UnreliableCar

File: `unreliable_car.py` and `unreliable_car_test.py`

Let's make our own derived class for an **UnreliableCar** that inherits from **Car**. Write Python code for this class
in a new file,
`unreliable_car.py`, and write some testing code in
`unreliable_car_test.py` to verify each method.

**UnreliableCar** has an additional attribute:

- **reliability**: a **float** between 0 and 100, that represents the percentage chance that the `drive` method will
  actually drive the car

**UnreliableCar** should override the following methods:

- **`__init__(self, name, fuel, reliability)`**

    - call the Car's version of **`__init__`**, and then set the reliability to the value passed in

- **`drive(self, distance)`**

    - generate a random number between 0 and 100, and only drive the car if that number is less than the car's
      reliability.  
      Don't store the random number! It's not a self/instance variable that you want to remember, it's a temporary value
      you generate and use once, every time you call `drive()`.

    - **Super Important Note:** the drive method in the base class
      (Car) ***always*** returns the distance driven, so your derived class
      (UnreliableCar) must also return a distance. You must match the "signature" of any method you override.  
      This is true, even if your UnreliableCar drives 0 km.

## SilverServiceTaxi

File: `silver_service_taxi.py`

Now create a new class for a **SilverServiceTaxi** that inherits from
**Taxi**. Do you see the pattern for naming class files?

So **SilverServiceTaxi** *is a* **Taxi** and **Taxi** *is a* **Car**
(which means **SilverServiceTaxi** is a **Car**)

This allows you to have a different effective `price_per_km`, based on the fanciness of the **SilverServiceTaxi**.

1. Add a new *attribute*, `fanciness`, which is a `float` that scales (multiplies) the `price_per_km`. Pass
   the `fanciness` value into the constructor and multiply
   `self.price_per_km` by it.  
   Note that here we can get the initial base price using
   `Taxi.price_per_km`, then customise our object's instance variable,
   `self.price_per_km`. So, if the class variable (for all taxis) goes up, the price change is ***inherited*** by all
   SilverServiceTaxis.  
   If you're not sure about this, please ask! Don't go on without "getting it".

2. **SilverServiceTaxis** also have an extra charge for each new fare, so add a `flagfall` *class variable* set to
   $4.50.

3. Add or override whatever method you need to (think about it...) in order to calculate the fare.

4. Create an overridden `__str__` method so that you can add the `flagfall`
   to the end. E.g., for a Hummer with a fanciness of 4, it should display like:

       Hummer, fuel=200, odo=0, 0km on current fare, $4.92/km plus flagfall of $4.50

   Note that you can reuse the parent class's `__str__` method like:
   `super().__str__()`

5. Write some test code in a file called `silver_service_taxi_test.py` to see that your
   **SilverServiceTaxi** calculates fares correctly.  
   For an 18 km trip in a **SilverServiceTaxi** with fanciness of 2, the fare should be $48.78 (yikes!)

Let's stop and think about what we've done and (hopefully) learned so far:

- We can create new classes by *extending* existing ones - e.g. Taxi extends Car

- Derived (child) classes inherit all the attributes and behaviours of their base (parent) classes - e.g. we do not need
  to write a new
  **`add_fuel()`** method for Taxi because it comes from Car already, and we don't need anything different in a taxi.

- We can *override* (customise) derived classes by modifying existing methods so that they do different (but similar)
  things.  
  We should always make sure that the signature of overridden methods matches the base class - e.g., the **`drive()`**
  method in Taxi also calculates a fare, and in UnreliableCar it may or may not drive any distance... but in ***all***
  cases, the method takes in a distance value and returns the distance driven.

Here is what the **class hierarchy** looks like now for **Car** and its related classes (remember you can "read" these
arrows like "Taxi *is a* Car"):

![Car class hierarchy diagram](../images/08image1.png)

## Inheriting Enhancements

One more thing before we move on... (_Are you still reading/learning carefully?_)

It's important to see how using inheritance actually benefits the systems we model with classes.  
Currently, all Taxis (including SilverServiceTaxis and any other derived classes we might make) calculate the fare
as `price_per_km * current_fare_distance`, and you can get results like $48.78 in the example above...

What if we decided that all taxis should have final fares that are rounded to the nearest 10c (so that $48.78 would
change to $48.80)?  
Well, we should only need to make this change to the base Taxi class, and it will be inherited by
SilverServiceTaxis... *but only if* we have called **`super().get_fare()`** and not rewritten the calculation in our new
classes. That is, we should only need to change one place because we should have practised the "Don't Repeat Yourself" (
DRY) principle.  
If we didn't call the super method, but just repeated the calculation, then changing the base class will *not* change
the derived class!
Make sense? Let's do it.

- First, run your silver_service_taxi_test program from above and make sure your output produces something that's not
  already a multiple of 10c (such as the example above that produces $48.78).

- Now update the **`get_fare()`** method in Taxi and make it use the
  **`round()`** function to return a value rounded to 10c.

- Re-run your test, and you should get a result rounded to 10c (e.g., $48.80). If it worked, you should see that we only
  changed Taxi and that enhancement was inherited by SilverServiceTaxi. Nice :)

### Yet Another Important Note About Functions

**`get_fare()`** must return a *number*, not a *string*!  
Even though we may want to format the result like currency (e.g. `"$48.80"`), that's not this function's single
responsibility. What if we wanted to add fares together? They must be numbers. Do your string formatting *outside* this
function.

*Keep going!*

# Do-from-scratch Exercises

File: `taxi_simulator.py`

Write a taxi simulator program that uses your **Taxi** and
**SilverServiceTaxi** classes.

Each time, until they quit:

- The user should be able to choose froma *list* of available taxis,

- They can choose how far they want to drive,

- At the end of each trip, show them the trip cost and add it to their bill.

Note: Use a list of taxi objects, which you create in main and pass to functions that need it. When you choose the taxi
object, your code will call the `drive()` method on that object, and it will use the right method for that class... so
from the client code point of view, driving a taxi will work the same whether the object is a Taxi or a
SilverServiceTaxi, but the results (including the price) depend on the class.  
This is ***polymorphism***.

Another note: In this program, there's the chance the user will  
drive a taxi before choosing one. This shouldn't crash.  
A good option is to maintain something like a `current_taxi`... but what will the initial value of this variable be?  
When you want a default starting value for an object, you use `None`:

    current_taxi = None

The taxis used in the example below would be like:

    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

### Sample Output (to show you how to write your program):

    Let's drive!
    q)uit, c)hoose taxi, d)rive
    >>> d
    You need to choose a taxi before you can drive
    Bill to date: $0.00
    q)uit, c)hoose taxi, d)rive
    >>> P
    Invalid option
    Bill to date: $0.00
    q)uit, c)hoose taxi, d)rive
    >>> c
    Taxis available: 
    0 - Prius, fuel=100, odometer=0, 0km on current fare, $1.23/km
    1 - Limo, fuel=100, odometer=0, 0km on current fare, $2.46/km plus flagfall of $4.50
    2 - Hummer, fuel=200, odometer=0, 0km on current fare, $4.92/km plus flagfall of $4.50
    Choose taxi: 3
    Invalid taxi choice
    Bill to date: $0.00
    q)uit, c)hoose taxi, d)rive
    >>> c
    Taxis available: 
    0 - Prius, fuel=100, odometer=0, 0km on current fare, $1.23/km
    1 - Limo, fuel=100, odometer=0, 0km on current fare, $2.46/km plus flagfall of $4.50
    2 - Hummer, fuel=200, odometer=0, 0km on current fare, $4.92/km plus flagfall of $4.50
    Choose taxi: 0
    Bill to date: $0.00
    q)uit, c)hoose taxi, d)rive
    >>> d
    Drive how far? 333
    Your Prius trip cost you $123.00
    Bill to date: $123.00
    q)uit, c)hoose taxi, d)rive
    >>> c
    Taxis available: 
    0 - Prius, fuel=0, odometer=100, 100km on current fare, $1.23/km
    1 - Limo, fuel=100, odometer=0, 0km on current fare, $2.46/km plus flagfall of $4.50
    2 - Hummer, fuel=200, odometer=0, 0km on current fare, $4.92/km plus flagfall of $4.50
    Choose taxi: 1
    Bill to date: $123.00
    q)uit, c)hoose taxi, d)rive
    >>> d
    Drive how far? 60
    Your Limo trip cost you $152.10
    Bill to date: $275.10
    q)uit, c)hoose taxi, d)rive
    >>> c
    Taxis available: 
    0 - Prius, fuel=0, odometer=100, 100km on current fare, $1.23/km
    1 - Limo, fuel=40.0, odometer=60.0, 60.0km on current fare, $2.46/km plus flagfall of $4.50
    2 - Hummer, fuel=200, odometer=0, 0km on current fare, $4.92/km plus flagfall of $4.50
    Choose taxi: 2
    Bill to date: $275.10
    q)uit, c)hoose taxi, d)rive
    >>> d
    Drive how far? 61
    Your Hummer trip cost you $304.60
    Bill to date: $579.70
    q)uit, c)hoose taxi, d)rive
    >>> c
    Taxis available: 
    0 - Prius, fuel=0, odometer=100, 100km on current fare, $1.23/km
    1 - Limo, fuel=40.0, odometer=60.0, 60.0km on current fare, $2.46/km plus flagfall of $4.50
    2 - Hummer, fuel=139.0, odometer=61.0, 61.0km on current fare, $4.92/km plus flagfall of $4.50
    Choose taxi: 1
    Bill to date: $579.70
    q)uit, c)hoose taxi, d)rive
    >>> d
    Drive how far? 59
    Your Limo trip cost you $102.90
    Bill to date: $682.60
    q)uit, c)hoose taxi, d)rive
    >>> Q
    Total trip cost: $682.60
    Taxis are now:
    0 - Prius, fuel=0, odometer=100, 100km on current fare, $1.23/km
    1 - Limo, fuel=0, odometer=100.0, 40.0km on current fare, $2.46/km plus flagfall of $4.50
    2 - Hummer, fuel=139.0, odometer=61.0, 61.0km on current fare, $4.92/km plus flagfall of $4.50

# Practice & Extension Work

## First, a Walkthrough Example - Files & Classes

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
  module and a `namedtuple`. Read through them if you're interested!

## Modifications

1. Add another language to the file - and make sure it still works properly. Use data from
   [this Programming Language Comparison page](http://www.jvoegele.com/software/langcomp.html)

2. Add another attribute to your ProgrammingLanguage class: **Pointer Arithmetic** (see that page or search to find is
   the language has it or not).  
   This will take a bit of effort, as you need to update the class and any code that uses it. You also need to add the
   correct values to your data file (it's similar to reflection).

## More Guitars!

Open the file: `guitars.csv`  
This file contains lines like:

`Fender Stratocaster,2014,765.4`

So, the format/protocol is:

`Name,Year,Cost`

1. Write a program to read all of these guitars in and store them in a list of tuples.  
   Display all the tuples using a loop.

2. Write another version (save a new copy) that stores them in a list of Guitar objects, using the class that you wrote
   in practical 6 recently.  
   Display these using a loop.

   Now **sort** the list by year (oldest to newest) and display them in sorted order...  
   How do you do that? Sorting requires that Python knows how to compare objects...  
   If we just use:

   `guitars.sort()`

   We get an error like:

   `TypeError: unorderable types: Guitar() < Guitar()`

   So we need to define how the `<` operator should work.  
   Do you remember how?

   Write code for the `__lt__` (less than) method. You should be able to figure this out...  
   Then test and see if it sorts correctly now.

3. Save a copy of this program as `myguitars.py` then modify this version so that it does the above, then asks the user
   to enter their new guitars (just like your practical 6 code).  
   Store these in your list of guitar objects, then  
   write all of your guitars to the file `myguitars.csv`.  
   Test that this worked by opening the file, and also by running the program again to make sure it reads the new
   guitars.

## Inheritance

### Cars

Create more kinds of cars that make sense to you and test them, e.g. select from:

a.  **GasGussler** - uses more fuel than it should

b.  **Bomb** - doesn't actually move when you drive it, but still uses the fuel

c.  **EcoTaxi** - uses half the fuel and gives a percentage discount on the price per fare

d.  [CrazyTaxi](https://en.wikipedia.org/wiki/Crazy_Taxi)

### Trees

The focus of this exercise is on inheritance - looking for what methods need to be changed (overridden) in the derived
classes. Don't get hung up on the details of the methods...

Trees: some grow wide, some grow thin; some grow fast, some grow slow.

**Open these two files:** [trees.py](trees.py) and [trees_tester.py](trees_tester.py)

trees.py contains the **Tree** class. A Tree object has a
**trunk_height**, and a number of **leaves**.  
The **`__str__`** method of **Tree** returns a string representation of the **Tree**. For example, if **trunk_height**
is 2, and leaves is 8, the Tree would look like

    ##
    ###
    ###
     |
     |

The size of a **Tree** can be changed by calling the **grow** method, which takes in **sunlight** and **water** and
randomly increases the
**trunk_height** and leaves.

Not all Trees look the same or grow the same, however, so we're going to build specialised classes to represent
different types of trees. To achieve this, we're going to use inheritance.

There are already two completed subclasses of **Tree** in trees.py:

**EvenTree**
Even trees only grow leaves in multiples of three, that way the leaves always appear in clean rows.

**UpsideDownTree**
Upside-down trees are drawn upside-down.

`trees_tester.py` grows **seven** types of trees. Try running it now. The final four types of trees are subclasses of **
Tree** for you to complete:

1. **WideTree**

   a. Wide trees grow their leaves in rows of six, and have a trunk that is twice as wide as normal trees

   b. You will need to redefine the `get_ascii_trunk` and
   `get_ascii_leaves` methods

   c. Example drawing:

         ####
         ######
         ######
           ||
           ||

2. **QuickTree**

   a. Quick trees grow much quicker than normal trees - their leaves always increase by however much sunlight falls on
   them, and their trunks always grow by however much water they receive.

   b. You will need to redefine the **grow** method.

   c. Quick trees look exactly the same as normal trees, they just grow differently.

3. **FruitTree**

   a. Fruit trees have a number of `fruit`

   b. Add a `fruit` variable to the **FruitTree** class; initialise it as 1

   c. Fruit trees sometimes gain an additional fruit when the **grow**
   method is called, the chance is 1 in 2

   d. Fruit trees sometimes lose a fruit when the `grow` method is called, the chance is 1 in 5

   e. Example drawing (fruit are represented by a dot `.`)    
   the fruit should be displayed the same way as the leaves, wrapping within the maximum width

        ..
        ###
        ###
         |
         |
         |

4. **PineTree (challenge)**

   a. pine trees look like

           *
          ***
         *****
        *******
           |
           |    

   b. pine trees start off with four leaves (1 + 3)

   c. pine trees only ever add as many leaves as would make a full new row at the bottom of the tree

   i. i.e. they must form a triangle shape

   ii. row 1 always has 1 leaf, then 3 for row 2, 5 for row 3, 7 for row 4, 9 for row 5 and so on

   iii. every time the `grow` method is called, the pine tree should add a new row of leaves if a random number between
   0 and sunlight is bigger than 2

### Taxi Simulator Enhancements

Enhance your taxi driving program so that it:

- doesn't let you drive until you've chosen a taxi

- has error-checking for choosing a valid taxi

- keeps track of the number of km you've done (actual distance driven not total requested)

- displays the taxis with their costs (`flagfall` and `fanciness`)

# Deliverables

This section summarises the expectations for marking in this practical.

- `taxi_test.py`
- `taxi.py` modifications (including class variable)
- `unreliable_car.py` & `unreliable_car_test.py`
- `silver_service_taxi.py` & `silver_service_taxi_test.py`
- `taxi_simulator.py`
# Practical 10 - Testing, APIs, Flask

Don't forget to make a new branch, `prac_10_feedback` _before_ you start.  
You will put some files into that branch for your normal practicals project/repo, but you will also have separate
projects and repositories for the Flask tasks.

Today we will explore the use of tools for **testing**, an **API** for Wikipedia and the very cool **Flask** Web
framework.  
But first, let's reflect on the subject so far...

# Reflection

Create a `README.md` markdown file in your `prac_10` folder.

Add the heading, `# Reflection`.  
Write short but thoughtful answers to each of the following:

1. Regarding the **estimates** that you did for practical tasks, how was your accuracy and did your accuracy improve
  during the course of the subject? What did you learn from doing the estimates?
2. Regarding **code reviews**, what have you learned from both being reviewed and doing reviews? 
3. Regarding the **practical tasks** overall, what would you change if you were in charge of the subject?

Next, add the heading, `# Code Reviews`.  
Provide proper Markdown links (not bare URLs) to two (2) PRs that show you doing good code reviews for any of the past pracs.  
For each one, write a short explanation of what was good about your review.  

# Testing

Copy [testing.py](testing.py) into your `prac_10` folder, then follow the `TODO` instructions in it, taking note that
the code shows you examples to learn form.

1. Fix the `repeat_string` function so that it passes the `assert` test.

   **Don't change the test!**  
   The failing test shows that the function is broken; fix the function.

2. Write at least two `assert` statements to show if `Car` sets the fuel correctly.

3. Uncomment the `doctest.runmod()` line to see how the doctests run.
   > [!NOTE]
   > PyCharm might detect your tests and automatically run your program in doctest mode.

4. Fix the failing `is_long_word` function.

5. Write and test (using doctest) a function to format a phrase as a sentence - starting with a capital and ending with
   a single full stop. See the comments for how to do this step by step, taking note that you should write your tests _
   before_ your code.  
   E.g., the function should change "hello" into "Hello."

# Wikipedia API & Python Library

File: `wiki.py`

> [!NOTE]
> We are interfacing with systems outside our control.  
> Some of the specific details here may change with different versions of the APIs we use.

Until now, we've only worked on our local computers, interacting with local files, but never talking to the great big
computer in the sky... so let's do that now :)

Many systems have public **APIs** (Application Programmer Interfaces) that we can use. An API is usually a set of
functions that
we can call to send and receive data to and from a system. You can write code to interact with things like Twitter,
Slack, weather services, government databases, NSA spy satellites and more...

We'll start with Wikipedia.

Instead of writing our own HTTP calls to the Wikipedia API, we can make use of a Python library that abstracts the
details away and presents a simpler, Python-based, API for us. *We need to install that now*.

The lab PCs should let us install packages. If it looks like the package is still installing (infinitely), just carry on
as if it were finished, and it should work... or just restart PyCharm if you'd like it to stop telling you it's
installing! If you really can't install the wikipedia package, then skip those parts of the prac that use it.

In PyCharm, go to Settings/Preferences > Project: Practicals > Project Interpreter (it might look a bit different, but
you should have been here before) and click the plus button to install a package. Type "wikipedia"
to find the one we want, and then click "Install Package".

> [!NOTE]
> If you don't have permission to install this, try it with the option to install to user's site packages directory.

![PyCharm install package](../images/10image3.png)

The quick start documentation for the wikipedia package can be found at:
<https://wikipedia.readthedocs.io/en/latest/quickstart.html>

As this documentation shows, a good way to learn a new package like this is via the console. Open the console in
PyCharm, then follow the docs and quickly try out functions like `search()`, `summary()` and `page()`.  
Get a page and see what properties it has.

**Create a new file** called `wiki.py` and write a small script that prompts the user for a page title or search phrase,
then prints the summary of that page. Use a simple loop that continues doing this until the user enters blank input.

Try this with a few page titles and see what happens.  
(You might get a warning about an outdated use of the `BeautifulSoup` package. We can't fix that so please ignore it.)

Try it with the search/title "Python", and you should find that the Wikipedia API returns a "disambiguation" page, so
you
need to handle that **exception** as explained in the API's docs.

When getting a `page`, you might find that you get an unexpected result because the API has used `suggest()`
to suggest a particular page, different from what you asked for. You can customise how the page is determined, example:

    wikipedia.page(title, autosuggest=False)

Now **modify** your program so that when it gets the page, it prints the title, summary and the URL.

# Flask Web Framework

Until now, we have made only one type of project, "Pure Python", and we always interacted via PyCharm with the console
or using a GUI we made with Kivy.  
A very common way to deliver software these days is via a Web browser.  
Some programming languages are designed for the Web - like JavaScript for the browser and PHP for Web servers, but we
can
also use Python... if we use it via a "Web Framework".

There are a number of great frameworks, like Django, Web2Py and Pyramid, Today we will use **Flask**.  
(You may be interested to know that [WakaTime](https://wakatime.com)
is written in Python and uses Flask.)

Flask docs are at: <http://flask.pocoo.org/docs>.

In PyCharm, create a new project, choosing Flask.
> [!NOTE]
> You need the Professional edition, not the Community
> edition to see this screen when making a new project.

If this is the first time you've done this, PyCharm should
install the Flask package and other dependencies, like Jinja for templating.

![New Flask Project window](../images/10image4.png)

The default project comes with a folder structure and a simple "hello world" example like:

```python
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

```

## Explanation

After importing, we create an instance of the `Flask` class called `app`, passing the name of this module.

`@` is used for what's called a **"decorator"**.

This decorator is metadata about the function below it.  
In Flask, the `@app.route` decorator specifies the URL that will result in that function being called.

Then we have a normal function (`hello_world()`), but importantly it returns a string.                          
All Flask "views" (functions that will be displayed in the browser) must return strings.

Running a Flask app (`app.run()`) looks similar to Kivy, doesn't it?

Run the code, and you should see output like the following, including a link to click on to see your amazing new
Python-based website. Click the link in the Python console to view "Hello World!" in your browser.

`* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)`

Modify the function output to return `<h1>Hello World :)</h1>` and rerun the program by pressing Ctrl+F5 (or your IDE's
rerun shortcut).  
To see the new results, you'll need to go back to your browser and hit refresh, so do this now.

As you should see, pages/views are created using HTML. Learning HTML is beyond the scope of this prac, so hopefully you
already know some.

Make another view function by using the 'route' shortcut... that is, type 'route' and wait for the popup, then choose
the first option by pressing Enter... and PyCharm will create the decorator and function definition stubs.

![route autocomplete in PyCharm](../images/10image5.png)

Type 'greet' as the function name and route name (these can be different, but we'll keep them the same). Replace `pass`
with a simple
`return "Hello"` statement.

Re-run the program, then change your browser's URL by adding `/greet` to the end, like:

<http://127.0.0.1:5000/greet>

This is a bit simple so far... but we're getting there...

> [!NOTE] 
> If you ever get an "Internal Server Error" in the browser... this is *your* server (Python program)!  
> Go back to PyCharm and look for error messages in the console.

Add another decorator so that the greet function runs for multiple "sub"
routes and takes a parameter, like:

```python
@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"
```

Re-run and test with the URLs <http://127.0.0.1:5000/greet> and
<http://127.0.0.1:5000/greet/Yourname>

This is one way that you can pass string parameters to Flask view functions.

## Challenge

In an earlier prac, you wrote a function to convert between Fahrenheit and Celsius. Copy this function (as a
regular function, not a route) into your program.  
It should take a Celsius float value and return a Fahrenheit float.

Now, create a new route so that you can enter Celsius values in the URL and see the Fahrenheit values in the Web page,
like below. Note that the parameter passed via the URL (`100.2` in this case) is a string.

**SRP!** If you wrote the temperature conversion function correctly before... here's another great example of how
SRP works. We don't know or even care what the function will be used for - Flask, Kivy, Console... that's why we design
the function to do one job - just the conversion.  
If you did not write it correctly, then notice how you cannot reuse it.

![Fahrenheit conversion in website view](../images/10image6.png)

That's version 1... Once it works, modify it so the output shows the input value and the result with useful text.

Share this project on GitHub.  
You should submit the URL to this repo.

## Flask + Wikipedia API

Now let's combine the Wikipedia API with our new-found Web programming powers...

**Fork** the demo from
<https://github.com/lindsaymarkward/flaskdemo>

Then **clone** it so that you can work on it locally.

Run it and test it, then study the code to find a few new things:

- This demo uses **Jinja** HTML templates, which make formatting Web page outputs much nicer than hard-coding them in
  Python.

- It also uses "template inheritance", so that you can reuse parts of templates in other templates. That's how the
  navigation and footer persist.

- The search route has an HTML form in it. When it's submitted, it sends the data via the HTTP "post" method, so the
  route has to be customised to accept this. It then gets the data from the "request"
  object.

- `url_for()` is a function that returns the correct URL for a given view/route function so that you don't have to know
  the exact path.

### Modifications

Now it's your turn to make this more interesting and appealing. What else could you do to it?

- Start by adding the page title to the results

- Then add some details to the **about** page using a new template

- Then add a link to the about page in your layout template

- Then go crazy... :)

Before you go... have you completed the **YourJCU subject survey** for this and your other subjects?  
If not, please do that right now on LearnJCU.  
***Thank you... your input is extremely valuable!***

# Practice & Extension Work

1. Add `assert` and `doctest` testing to your work from an earlier prac - e.g., the `is_valid_password()`
   function.

2. During the holidays you might like to experiment with Flask and see if you can make some cool Web interfaces for your
   existing programs...

   A **great idea** would be to make programs with 3 interfaces: Console, Kivy and Web, and reuse as much common code as
   you can. That should help you see how modular your work is. This would help you understand "separation of concerns"
   more, as you just want to create 3 different views that use the same core functionality.

# Recursion

In previous years, this subject has covered **recursion**, but we've since moved that topic to a later programming
subject.  
Here are some questions relating to recursion, just for fun.

### Explore recursion

Open `recursion.py` and read the code, then **write down** (on paper, like it's a practice exam question!) the expected
output for the first function, `do_it(5)` **BEFORE** you run it.

Then run it to see if you were right.

Then use the **debugger** to step through the execution to see what's happening.

Do the same for the next function - start by uncommenting
`# do_something(4)`

You'll find a problem... The function should print the squares of positive numbers from n down to 0, but instead it runs
until the maximum recursion limit is reached...  
**Fix this.**

Write another version of this that recursively prints the squares backwards
(i.e., on the way back after hitting the base case).

### Pyramid program

![Pyramid](../images/10image2.png)

Write a program to get the number of rows from the user and calculate the number of blocks you will need to make a 2D
pyramid given this number of rows (n).

**Do this first as a simple loop in a function**, then **write a recursive function** to calculate the number of blocks.
As always, think about good function design. It should **take in** the number of rows and
**return** the number of blocks**.**

The number of blocks for n rows is:

`n + (n-1) + (n-2) + ... 2 + 1`

E.g., for 6 rows, it is 6 + 5 + 4 + 3 + 2 + 1 = 21

### Other recursive challenges

1. Write a recursive program that prints a string from the outside in.  
   E.g., if the string to print is `"Programming"`, your program should print: `"P g r n o i g m r m a"`.  
   Another example:

       Enter a string: 123456  
       1 6 2 5 3 4  

   Remember to analyse and design this problem first. Think about the base and recursive cases - when will it stop (
   base) and how will it reduce the problem (recursive) each time?

2. Write a recursive function to check whether a string is a palindrome.  
   A palindrome is a word or phrase that reads the same forwards as backwards. The following are examples:

    - Hannah
    - abcba
    - (ignoring case, spaces and punctuation) A Toyota's a Toyota

# Deliverables

This section summarises the expectations for marking in this practical.  
Please follow the [submission guidelines](../README.md#submission) to ensure you receive marks for your work.

Please submit the URL of your own feedback branch PR with a mention of a reviewer for this prac.

Files required:

Your non-Flask work goes in your normal practicals repo and should be part of a code review PR.  
Then, there's two separate Flask projects, which do not go in your practicals repo.  
Submit three URLs for these three (practicals PR, Flask project from demo, Flask + Wiki project)

- `README.md`
- `testing.py`
- `wiki.py`
- Flask project with modifications URL
- Flask + Wiki project URL

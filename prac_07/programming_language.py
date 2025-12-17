"""START

DEFINE a class called ProgrammingLanguage
    METHOD __init__(self, name, typing, reflection, year)
        SET self.name TO name
        SET self.typing TO typing
        SET self.reflection TO reflection
        SET self.year TO year

    METHOD __repr__(self)
        RETURN formatted string with name, typing, reflection, and year

    METHOD is_dynamic(self)
        IF self.typing EQUALS "Dynamic"
            RETURN True
        ELSE
            RETURN False

DEFINE FUNCTION run_tests()
    CREATE an object called ruby from ProgrammingLanguage with values: "Ruby", "Dynamic", True, 1995
    CREATE an object called python from ProgrammingLanguage with values: "Python", "Dynamic", True, 1991
    CREATE an object called visual_basic from ProgrammingLanguage with values: "Visual Basic", "Static", False, 1991

    STORE all language objects in a LIST called languages

    PRINT the string representation of the python object

    PRINT "The dynamically typed languages are:"
    FOR EACH language IN languages
        IF language.is_dynamic() IS True
            PRINT language.name

IF script is run as main program
    CALL run_tests()

END
"""

"""
CP1404/CP5632 Practical - Suggested Solution
Programming Language class with tests.
"""


class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name, typing, reflection, year):
        """Construct a ProgrammingLanguage from the given values."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Provide string representation of a ProgrammingLanguage."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def __repr__(self):
        """Provide developer-friendly representation of a ProgrammingLanguage."""
        return f"{vars(self)}"

    def is_dynamic(self):
        """Determine if language is dynamically typed."""
        return self.typing == "Dynamic"


def run_tests():
    """Run simple tests/demos on ProgrammingLanguage class."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(python)
    print(repr(python))
    # Use assert to ensure correct values are set and method returns correctly
    assert python.reflection is True
    assert python.is_dynamic() is True
    assert python.year == 1991
    assert ruby.reflection is True
    assert visual_basic.is_dynamic() is False


if __name__ == "__main__":
    run_tests()

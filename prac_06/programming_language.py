class ProgrammingLanguage:

    def __init__(self,name,type,reflection,year):
        self.name = name
        self.type = type
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.type == 'Dynamic'

    def __str__(self):
        # Python, Dynamic Typing, Reflection=True, First appeared in 1991
        return "{}, {} Typing, Reflection={}, First appeared in {}".\
            format(self.name,self.type,self.reflection,self.year)

"""Basic class stuff"""

class thing_class:
    
    # constructing
    # essentially the argument when initing the class is added, then we use the thing() function to print what that argument was, specifically a string.
    def __init__(self, thingy):
        self.thingy = thingy
    
    def thing(self):
        print(f"This is a", self.thingy)


t = thing_class('thing')
t.thing()

"""
Functions and Global Variables.
Globally resolved variables are read only. To change their values we use
in order to change that value we use the glabal keyword.  
"""
l = 10  # global variable - can be used by any part of the code. l is Global scope.


def add(a, b):
    """
    This is called as Docstring
    """
    l = 50  # local scope.It searches for local scope then it goes for global
    return a + b


print(add(3, 5))

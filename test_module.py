"""
    Filename: test_module.py

    This file is for you to use as you experiment with single file modules 

    Initially it contains some module variables, and a few lines of code
    
    This string is docstring for the module and will be in the module objects `__doc__` property

"""

A_CONSTANT = 42       # Using all caps indicates that this should not be changed (but you can)

counter = 0           # this could be changed

_private_counter = 0  # starting the name with '_' makes it *more* private (but again, you can get at it if you want)


counter += 1
print(f"counter is {counter}")


import sys

def return_source_module():
    """ This function uses the sys.modules dictionary to return 
        the module that contains this function
    """
    return sys.modules[__name__]
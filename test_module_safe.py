"""
    Filename: test_module_safe.py

    2. The first task is to rework test_module.py to create a ‘safe’ module (test_module_safe.py) 
        where on import the only code executed is setting the variables, not the incrementing and 
        printing of counter, which should be in a function controlled by an if statement that checks 
        the module’s __name__ property.

    When creating a safe module, keep the following steps in mind:
        Any code that you don’t want automatically executed should go into a function or a class. About 
        the only thing that should be left outside of functions is initializing variables that will be 
        accessible to the entire module.
        If you do want the module to be a standalone script, you can check the __name__ variable in the 
        module namespace. The if statement if __name__ == '__main__' is true if the module is being run 
        as the main script and should execute some code or call functions or methods.

    This string is docstring for the module and will be in the module objects `__doc__` property
"""

import sys


A_CONSTANT = 42       # Using all caps indicates that this should not be changed (but you can)

counter = 0           # this could be changed

_private_counter = 0  # starting the name with '_' makes it *more* private (but again, you can get at it if you want)




def show_counter():
    """This function shows the module's counter value"""
    print(f'counter is {counter}')

def increment_counter():
    """This function increments the module's counter value by one"""
    global counter
    counter += 1

def return_source_module():
    """ This function uses the sys.modules dictionary to return 
        the module that contains this function
    """
    return sys.modules[__name__]


if __name__ == '__main__':
    increment_counter()
    #counter += 1
    show_counter()
    #print(counter, A_CONSTANT, _private_counter)

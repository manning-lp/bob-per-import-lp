# CONTENTS OF simple_module.py


def module_function():
    print("hello from the module's function")
    
if __name__ == "__main__":
    print("running as main program, calling module's function")
    module_function()
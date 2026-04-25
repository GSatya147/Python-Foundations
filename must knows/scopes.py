# SCOPES
'''
LEGB
Local, Enclosing, Global, Built-in - python follows same order to check a particular variable's scope
'''

x = 'global x'

def test():
    # python doesn't override global x, local x is a different one
    x = 'local x'
    y = 'local y'
    print(y) # 'local y'
    print(x) # 'local x' - python checks whether there is a local x, enclosing, global x and built-in x

test()
# print(y) # Nameerror
print(x) # 'global x'

def test2():
    global x # declaring that we are working with global x here
    x = 'local x' # now global value gets overriden
    print(x) # 'local x'

test2()
print(x) # 'local x' - cus got overriden

"""
Note: even if global x value doesn't exists prior to declaration of local x,
the "global x" st itself sets the next x declaration as global scope 
"""

# variables created inside func are local scope

# -------------------------------------------------------------------------------------------------------------
# Built-in scope

import builtins

print(dir(builtins)) # returns a list of the attributes of builtins module
# Try not to declare varaibles with built-in names

# python checks for global scope before built-in scope, can cause conflicts unknowingly
# eg - min function

def min():
    pass

# User expects min to find min of list
print(min([1, 2, 3])) # gives error, python thinks min as user built func instead standard min

# --------------------------------------------------------------------------------------------------------------
# Enclosing scope - nested structures

def outer():
    x = 'outer x'

    def inner():
        """Python checks for local x, can't find any.
           hence goes with the enclosing scope, i.e enclosing func scope - outer()
        """
        print(x) 
    
    inner()
    print(x) 

outer()

# -----output-------
# outer x
# outer x

#----------------------------------------------------------------------------------------------------------------
# nonlocal keyword

def outer():
    x = 'outer x'

    def inner():
        nonlocal x # declares we are working with enclosing x not local x
        x = 'inner x'
        print(x) 
    
    inner()
    print(x) 

# -----output-------
# inner x
# inner x

# honestly 'nonlocal' is more useful than 'global' lol
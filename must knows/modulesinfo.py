import sys
"""
When imported, all the print sts are executed
import cases:
1. import module
2. import module as m
3. from module import func1, func2
4. from module import func1 as f1
5. from module import *

"""

# python looks for all the paths, can check the list of directories that py checks for imports using 'print(sys.path)'
print(sys.path)

# If module not found, we can add the path of the module present to sys
sys.path.append("/path/Desktop/Modules")

# Alternatively can export a PYTHONPATH variable with the explicit path, more efficient
"""
1. set a new environment variable named PYTHONPTH
2. set it to "C:\path\desktop\Modules"
3. now can import the modules present in Modules folder anywhere on the system
"""

# Can check the available paths again
print(sys.path)

# Some standard libraries:
# 1. Random:
import random

course = ["Math", "Art", "CompSci"]
random_course = random.choice(course)
print(random_course)

# 2. Math
import math

rads = math.radians(90)
print(math.sin(rads)) # sin 90

# 3. Datetime and Calendar
import datetime
import calendar

today = datetime.date.today()
print(today)

print(calendar.isleap(2017))

# 4. OS
import os

print(os.getcwd()) # to get present working directory

# To know the location of a module, for furhter exploration
print(os.__file__)

# To knwo all the methods, funcs in a module
print(dir(os))
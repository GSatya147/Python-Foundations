# STRINGS

string = """ 
multiline 
string
"""
print(string)

#slicing
print(string[1:4]) # includes 1 excludes 4 

#string methods
string.lower() # is a method
string.count('m') # return negative if absent
c = string.replace('l', 'b') # returns a new string

# concatenation
# 1: "+"
string + c

# 2: format - uses placeholders
d = "{}, {}. welcome!".format(string, c)

# 3: f strings
d = f"{string}, {c.upper()}. welcome!"

'''
To know all methods available on an object - dir(object), help(object.method) considering everyting is an object in py
'''
# Conditionals if-else, if-elif-else
"""
'==' is different from 'is'
is: Object Identity, checks for whether obj id is same in the memory
"""
a = 1
b = 1
a == b # true
a is b # false, cus different ids
id(a) is id(b) # false

a = b # copy
a is b # true
id(a) is id(b) # true 

# falsy values in conditionals
"""
False
None
Zero - 0
Any empty seq - '', (), []
Any empty mapping - {}
"""


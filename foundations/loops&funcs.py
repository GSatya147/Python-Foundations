# LOOPS

"""
1. break - stops and comes out of the loop
2. continue - skips the present iteration and continues the next iteration
"""

range(10) # 0 to 9
range(1, 10) # 1 to 9

for i in range(3):
    for j in range(3):
        print(f"matrix[{i}][{j}]")

# -------------------------------------
# FUNCTIONS

def hi():
    pass

hi() # executes hi
print(hi) # prints hi func object

# keyword and default values
def hi(name, greet = "hi"): # default value, used after keyword values only
    print(f"{greet}, {name}!")

hi("satya")

# for unknown number of positional and keyword args

# Use Case 1:
def hi(*args, **kwargs):
    print(args) # takes postional args, returns a tuple of positional args: ("Math", "Art")
    print(kwargs) # takes keyword args, name, age, returns dictionary of keywords and values: {"name": "Satya", age: 22}

hi("Math", "Art", name = "Satya", age = 22)

# Use Case 2:
course = ["Math", "Art"]
info = {
    "name": "Satya",
    "age" : 22
}
def hi(*args, **kwargs):
    print(args)
    print(kwargs)

hi(course, info) # both goes into *args as positional args as a tuple of a list and a dict
hi(*course, **info) # unpacks as we wanted

# leap year:
def is_leap(year):
    """Return true for leap else false"""
    return year % 4 ==0 and (year % 100 != 0 or year % 400 == 0)

print(is_leap(1900))




# DECORATORS
class Employee:
    def __init__(self, fname, lname):
        self.fname = fname 
        self.lname = lname
        # if user edits fname, lname, the full name wont be changed automatically, hence use a specific method fullname()
        # self.fullname = '{} {}'.format(fname, lname)

    # But if everytime we need to access fullname, we need fullname(), instead we can explicitly decorate the method to behave like an attribute ahha
    @property # Getter like - decides the route based on operator context
    def fullname(self): 
        return '{} {}'.format(self.fname, self.lname)
    
    @fullname.setter # Setter like
    def fullname(self, name):
        self.fname, self.lname = name.split(' ')

    @fullname.deleter # Accessed whenever del is used on full name
    def fullname(self):
        self.fname = None
        self.lname = None
        print('Deleted!')
    
emp1 = Employee('Satya', 'Gann')
emp2 = Employee('Veera', 'Gann') 

# Before decorator
# print(emp1.fullname())
# After decorator
print(emp1.fullname) # Getter called

# --------------------------------------------------------------------------------------------------------------------------------------------------
# Scenario: if we want to set fname, lname from a given full name

# RHS of assignment, name is passed as an arg to Setter
emp1.fullname = "Claude Sonnet" # Uses the setter to set the first name here in the specified format, and uses the setter to update the fname, lname
print(emp1.fname)
print(emp1.lname)

del emp1.fullname # Deleter called

"""
Note: Based on assignemnet operator, getter, setter and deleter are distinguished
    - assignment triggers setter
    - read/access triggers getter
    - delete triggers deleter
"""

# Special/dunder methods
class Employee:
    num_of_emps  = 0 
    raise_amount = 1.2 

    def __init__(self, fname, lname, pay):
        self.fname = fname 
        self.lname = lname
        self.pay = pay

        Employee.num_of_emps += 1 

    def fullname(self): # A class method
        return '{} {}'.format(self.fname, self.lname)
    
    def apply_raise(self):
        return self.pay * Employee.raise_amount
   
    def __repr__(self): # For representation of our clas - helps in debugging, logging
        return  "Hello, write the __str__  bruhh"# Used when __str__ is absent
   
    def __str__(self): # accessed whenever print is used in an instance, fallsback to __repr__ if absent
        return "Employee('{}', '{}', {})".format(self.fname, self.lname, self.pay)        

    def __add__(self, other): # acts for pointers for two instances
        return self.pay + other.pay
    
    def __len__(self):
        return len(self.fullname())

emp1 = Employee('Satya', 'Gann', 50000)
emp2 = Employee('Veera', 'Gann', 34000) 

# These are same
print(emp1)
print(emp1.__str__)
print(str(emp1))

# These are same
print(repr(emp1))
print(emp1.__repr__)
print(emp1) # repr is used only if str is absent

# ---------------------------------------------------------------------------------------------------------------
# Dunder intuition

# built-in class's dunder methods
# eg - 1
print(1 + 2)
print(int.__add__(1, 2))
print(str.__add__('hi', 'world'))

# eg - 2
print(len('test')) # 4
print('test'.__len__) # 4

# Hence we can add an dunder add method to add our custom objs
print(emp1 + emp2) # Here emp1 goes to self and emp2 goes to other
print(len(emp1))

# Can do with different dunder methods and define our own rules:

# one use case: datetime module has dunder add to add to date expliclty coded inside the date class, when + operator is used, operator overloading triggers adding two through rules defined in dunder add of date class

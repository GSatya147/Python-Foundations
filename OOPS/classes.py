 # CLASSES & INSTANCES
class Employee:
    """
    1. Class variables are variables that are shared between all the instances of a class
        - Can access via 'class.variable' & 'self.variable'
        - The instance created gets to use everything in that class, 
          hence class variables can be accessed by class and all the instance created (self), inside the class.
    2. Instance variables are unique to instances created
    """

    num_of_emps  = 0 
    raise_amount = 1.2 # A class variable

    def __init__(self, fname, lname, pay):
        self.fname = fname # An instance variable
        self.lname = lname
        self.pay = pay

        Employee.num_of_emps += 1 # Override class value once a variable is created

    def fullname(self): # A class method
        return '{} {}'.format(self.fname, self.lname)
    
    def apply_raise(self):
        return self.pay * Employee.raise_amount # Can also use self.raise amount

    @classmethod # A decorator - ability to define a method's behaviour
    def set_raise(cls, amount): # cls automatically takes class as arg like self takes instance as an arg
        cls.raise_amount = amount # reflects for all the instances

    @classmethod # if something is used always, best practice - automate it and make life easier
    def auto_create(cls, input_string):
        first, last, pay = input_string.split('-')
        return Employee(first, last, pay) # return the instance

    @staticmethod 
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

# Can have multiple instance variables
emp1 = Employee('Satya', 'Gann', 50000)
emp2 = Employee('Veera', 'Gann', 34000) 

# Both are same
emp1.fullname() # here emp1 is taken as argument in self, emp1 is the instance variable
Employee.fullname(emp1) 

# To distinguish class variables and instance
Employee.__dict__ # Returns variables of the class
emp1.__dict__ # Returns variables in the instance

"""
Note:
1. whenever 'Employee.raise_amount' is used, changing an instance's raise amount value won't influence the actual method
'''
Employee.raise_amount = 1.5 # will reflect every instance
emp1.raise_amount = 1.5 # Adds raise_amount into dict of instance, wont reflect other instances
'''
2. But using 'self.raise_amount' changes things, interesting...can override the value using instance's values
"""

Employee.num_of_emps # Returns total number of instances created, 2

# ----------------------------------------------------------------------------------------------------------------------------
# Regular methods - accessed by instances, has arg of instance in the form of self
# Class methods - can be accessed by both, regular methods with decors, has arg of class in the first positional arg

# Both will return same since set_raise is a class method
Employee.set_raise(1.5)
emp1.set_raise(1.5) 

# Use Case - using class method as an alternative constructor
# scenario - want to create an instance through string format, considering we inly get a string in form of hyphens

# Brute force:
emp_string = 'Joe-Doe-7000'
first, last, pay = emp_string.split('-')

emp3 = Employee(first, last, int(pay))
print(emp3.fullname())

# Class method: Alternative constructor
# don't forget to return the instance, don't be like claude dumbahh..haha
new_emp = Employee.auto_create(emp_string)
print(new_emp.fullname())

# ----------------------------------------------------------------------------------------------
# Static methods - magic, don't need any prerequisited args
import datetime

my_date = datetime.date(2026, 4, 25)

print(Employee.is_workday(my_date))

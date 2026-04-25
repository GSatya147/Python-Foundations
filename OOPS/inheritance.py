 # INHERITANCE
class Employee:
    num_of_emps  = 0 
    raise_amount = 1.2

    def __init__(self, fname, lname, pay):
        self.fname = fname 
        self.lname = lname
        self.email = '{} {}'.format(fname, lname)
        self.pay = pay

        Employee.num_of_emps += 1 

    def fullname(self): # A class method
        return '{} {}'.format(self.fname, self.lname)
    
    def apply_raise(self):
        return self.pay * Employee.raise_amount 

class Developer(Employee): # gets everything inherited, any changes here wont effect parent class
    def __init__(self, fname, lname, pay, prog_lang):
        # both are same
        # Employee.__init__(self, fname, lname, pay)
        super().__init__(fname, lname, pay) # DRY - don't repeat yourself, don't copy and paste from Employee class, use super()
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, fname, lname, pay, employees = None): # Never pass mutable datatypes as default parameters, use None instead
        super().__init__(fname, lname, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
        else:
            print('Employee is already in the list.')

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
        else:
            print('Employee is not in the list.')

    def print_emp(self):
        for emp in self.employees:
            print('-->', emp.fullname())

# To investigate Sub classes - can also see method resolution order
print(help(Developer))

dev_1 = Developer('Veera', 'Gann', 45000, 'Python')
dev_2 = Developer('Satya', 'Gann', 34000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
mgr_1.add_emp(dev_2)

print(isinstance(mgr_1, Employee)) # True
print(isinstance(mgr_1, Developer)) # False

print(issubclass(Manager, Employee)) # True
print(issubclass(Manager, Developer)) # False
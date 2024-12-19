class Employee():

    def __init__(self, name, salary):

        self.name = name
        self.salary = salary
    def __str__(self):

        return print(f'employee name {self.name} , salary = {self.salary}')
    
class Manager(Employee):

    def __init__(self, name, salary, deparment_name):
        self.department_name = deparment_name
    
        super().__init__(name, salary)

    def __str__(self):
        
        return print(f'employee name {self.name} , salary = {self.salary}, head of {self.department_name}.')
    
class Developer(Employee):

    def __init__(self, name, salary, prog_lang, manager):
        self.prog_lang = prog_lang
        self.dep_head = manager

        super().__init__(name, salary)

        def __str__(self):

            return print(f'employee name {self.name} , salary = {self.salary}')
        
        
emp1 = Employee('john', 25000)
emp2 = Employee('dave', 25000)
man1 = Manager('susan', 35000, 'accounts')
dev1 = Developer('josh', 30000, 'python', man1)






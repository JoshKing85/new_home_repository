import math
class my_greeting():

    def __init__(self, your_name, prefered_food):

        self.name = your_name
        self.food = prefered_food


    def greet(self):

        print(f'Hello, {self.name}. Welcome to object orientated programming.')
        print(f'We heard you favourite food is {self.food}.')
        


first_person = my_greeting('Josh', 'bacon')
sec_person = my_greeting('Alex', 'pizza')

# first_person.greet()
# sec_person.greet()



class Circle():

    def __init__(self):
        self.radius = None
        


    def set_radius(self, radius):

        self.radius = radius


    def get_radius(self):

        return self.radius
    
    def area(self):

        return (3.14 * (self.radius ** 2)) 
    
    def __str__(self):

        return f'The circle has a radius of {self.get_radius()} with an area of {self.area()}'


circle_1 = Circle()
circle_1.set_radius(5)
# print(circle_1)


class Car():

    def __init__(self, brand, year):

        self.brand = brand
        self.year = year


    def describe(self):

        print(f'The car is a {self.brand} made in {self.year}')


car = Car('BMW', 2023)
# car.describe()


class Rectangle():

    def __init__(self, length, width):

        self.length = length
        self.width = width


    def area(self):

        return self.length * self.width
        

    def perimeter(self):

        return (self.length * 2) + (self.width * 2)
        
    def __str__(self):

        return f'The perimter of the rectangle is {self.perimeter()}cm, the area of the rectangle is {self.area()}cm.'
        

rec_1 = Rectangle(5, 3)

# print(rec_1)


class Bank_Account():

    def __init__(self, name, balance = 0):

        self.name = name
        self.balance = balance
        

    def deposit(self, dep_amount):

        self.balance += dep_amount

    
    
    def withdraw(self, wtd_amount):

        if self.balance >= wtd_amount:

            self.balance -= wtd_amount

        else: 
            print(f'Insuffecient funds to withdraw £{wtd_amount}')

    
    
    def check_balance(self):

        return print(f'Your current balace is £{self.balance}')


    
    def display_info(self):

        return print(f'Hello {self.name}, your current balance is £{self.balance}')


# customer_1 = Bank_Account('Josh', 100)

# customer_1.check_balance()
# customer_1.withdraw(10)
# customer_1.display_info()

# customer_2 = Bank_Account('John',)
# customer_2.check_balance()
# customer_2.withdraw(10)
# customer_2.deposit(150)
# customer_2.display_info()
    



class Animals():

    def __init__(self, name, age, sound):

        self.name = name
        self.age = age
        self.sound = sound

class Dog(Animals):

    def __init__(self, breed, age, name, sound):
        self.breed = breed
        super().__init__(age, name, sound)

    def display(self):

        print(f'name: {self.name}, age: {self.age}, sound: {self.sound}, breed: {self.breed}.')



dog_1 = Dog('Spot', 10, 'bark', 'labrador')
dog_1.display()


 





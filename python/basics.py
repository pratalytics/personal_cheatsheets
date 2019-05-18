# creating a variable
a = 1
b = 'c'

#Data structures
my_list = [1,2,3]
my_dict = {
  'name': 'John',
  'age': 32
}


## Creating a simple class
class Sample():
    pass
my_sample = Sample()

print(type(my_sample))

# <class '__main__.Sample'>

## Creating class with attributes

class Dog():

    def __init__(self, breed, name, spots):
        self.breed = breed
        self.name = name
        self.spots = spots
        
## Creating a class with class object attribute and methods
class Circle():

    #Class Object attribute
    pi = 3.141

    def __init__(self,radius=1):
        self.radius =radius

    def circumference(self):
        return 2 * self.pi * self.radius

    def area(self):
        return self.pi * (self.radius ^ 2)
      
# Inheritance and polymorphism

class Animal():

    def __init__(self):
        print("Animal Created")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print('I am eating')


class Cat(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Cat created")

    def who_am_i(self):
        print('I am a cat')

    def meow(self):
        print('Meow!')
      
      
 # Polymorphisim

class Crow():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return f'{self.name} says caw!'

class Cow():

    def __init__(self, name):
        self.name = name

    def speak(self):
        return f'{self.name} says moo!'

rookie = Crow('rookie')
bolu = Cow('bolu')

for pet in [rookie,bolu]:
    print(type(pet))
    print(pet.speak())


def pet_speak(pet):
    print(pet.speak())

pet_speak(rookie)


# Abstract Classes
class Fish():

    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Sub class must implement this abstract method")

class Prawns(Fish):


    def speak(self):
        return 'gubu gubu!'

my_fish = Prawns('Nemo')

# Special methods
#Using built in python functions with your own user defined functions

class Book():

    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    def __del__(self):
        print('A book object has been deleted')
        
# Class methods that change the object attributes
class Simple():

    def __init__(self, value):
        self.value = value

    def add_value(self, amount):
        self.value = self.value + amount

    def sub_value(self,amount):
        if (self.value - amount) > 0:
            self.value = self.value - amount
            print(f'Balance is {self.value}')
        else:
            print('Insufficient Funds')
            
# Module and packages
from MyMainPackage import some_main_script
from MyMainPackage.SubPackage import mysubscript

some_main_script.report_main()
mysubscript.sub_report()

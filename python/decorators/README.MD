# Decorators in python

Decorators allow you to "decorate" a function in python\
Imagine you created a function
```python
def simple_function():
    # Do some simple stuff
    return something
```
Now you want to add some more functionality to it or in other words add more code\
One way to do it is 
```python
def simple_function():
    # Want to do more stuff
    # Do some simple stuff
    return something
```
You have two options
* Add that extra code to your old function.\
Problem is you won't be able to call the old function as is as it has been modified
* Create a brand new function that contains the old code, and then add new code to that

### What if you want to remove that extra functionality?
In this case you would either need to delete it manually or make sure you have the old function\
_Is there a better way to do it?_

Python has __decorators__ that allow you to tack on extra functionality to an existing function\
They use __@__ operator and then are placed on the top of the existing function\
When you no longer want that functionality you delete that decorator line
```python
@decorator
def simple_function():
    # Do some simple stuff
    return something
```

Function inside a function
```python
 def hello(name='Sonia'):
    print('The hello function has been executed')

    def greet():
        return '\t This is a greet() function inside hello'

    def welcome():
        return '\t This is a welcome() function inside hello'

    print('I am going to return a function')
    if name == 'Sonia':
        return greet
    else:
        return welcome


var_a = hello('Prat')
print(var_a())
```
Pass function as an argument within another function
```python
def hello():
    return 'Hi Prats'

def other(some_def_func):
    print('Other code run here')
    print(some_def_func())

other(hello)
```

Complicated way of doing it
```python
def new_decorator(original_func):

    def wrap_func():
        print('Some extra code before the original function')
        original_func()
        print('Some extra code, after the original function')

    return wrap_func

def func_needs_decorator():
    print('I want to be decorated!!')

func_needs_decorator()

decorated_func = new_decorator(func_needs_decorator)
decorated_func()
```

Using the __@__ operator
```python
def new_decorator(original_func):

    def wrap_func():
        print('Some extra code before the original function')
        original_func()
        print('Some extra code, after the original function')

    return wrap_func

@ new_decorator
def func_needs_decorator():
    print('I want to be decorated!!')

func_needs_decorator()
```

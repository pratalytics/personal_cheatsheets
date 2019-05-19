# Python OOP overview

Creating a simple class
```python
class Sample():
    pass
my_sample = Sample()

print(type(my_sample))
```

Creating a class with attributes and methods

```python
class Circle():

    #Class Object attribute
    pi = 3.141

    def __init__(self,radius=1):
        self.radius =radius

    def circumference(self):
        return 2 * self.pi * self.radius

    def area(self):
        return self.pi * (self.radius ^ 2)
```

Magic/ Dunder Methods
```python
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
```

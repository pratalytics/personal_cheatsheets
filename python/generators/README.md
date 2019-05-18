# Generators in python
Generator functions allows us to write to a function that can send back a value and then later resume to pick up where it left off.\
The main difference in syntax will be use of the __yield__ statement.\
When a generator function is compiled they become an object that supports an iteration protocol.\
Generator functions are memory efficient
Example of not using a generator function
```python
def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result

print(create_cubes(11))

for x in create_cubes(11):
    print(x)
```
Simple generator function
```python
def create_cubes(n):

    for x in range(n):
        yield x**3


for x in create_cubes(11):
    print(x)
```

Generating a fibonacci sequence
```python
def gen_fibon(n):
    a = 1
    b = 1

    for i in range(n):
        yield a
        a,b = b, a+b

for num in gen_fibon(10):
    print(num)
```

Key to fully understanding generators - __next function__\
```python
def simple_gen():

    for x in range(3):
        yield x


for num in simple_gen():
    print(num)

g = simple_gen()

print(g)
print(next(g))
```

__iter function__
```python
s = 'hello'
s_iter = iter(s)
print(next(s_iter))
```

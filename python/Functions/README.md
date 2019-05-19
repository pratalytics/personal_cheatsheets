# Python Functions

### map Function
The __map__ function allows you to "map" a function to an iterable object. That is to say to you can quickly call the same function to every item in an iterable, such as an list.

```python
def square(num):
    return num**2
    
my_nums = [1,2,3,4,5]

map(square,my_nums)
# <map at 0x205baec21d0>

# To get the results, either iterate through map() 
# or just cast to a list
list(map(square,my_nums))
```

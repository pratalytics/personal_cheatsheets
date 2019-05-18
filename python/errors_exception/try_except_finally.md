### Three Keywords
__try__ This is the block of code to be attempted. (May lead to an error)\
__except__ Block of code will execute in case there is an error in the __try__ block\
__finally__ final block of code to be executed regardless of the the error

try execpt code block
```python
try:
    # want to attempt this code
    # May have an error
    result = 10 + 10
except:
    print('Hey it looks like you arent adding correctly')
else:
    print('Add went well')
    print(result)

```

try except finally block (with no errors). In this case the finally code block will run
```python
try:
    f = open('testfile', 'w')
    f.write('Writing a test line')
except TypeError:
    print('There was a type error')
except OSError:
    print('There was an OS error')
finally:
    print('I always run')
```

Now we induce an OS error
```python
try:
    f = open('testfile', 'r')
    f.write('Writing a test line')
except TypeError:
    print('There was a type error')
except OSError:
    print('There was an OS error')
finally:
    print('I always run')
```

Example
```python
def ask_for_int():
    while True:
        try:
            result = int(input('Please provide a number: '))
        except:
            print('That is not a number')
            continue
        else:
            print('Yes thank you')
            break
        finally:
            print('End of try/except/finally block')
            print('I will always run at the end')


ask_for_int()
```

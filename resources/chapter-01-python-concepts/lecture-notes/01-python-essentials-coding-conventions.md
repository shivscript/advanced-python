# Python Essentials - Complete Beginner's Guide

## Table of Contents
1. [Python Essentials](#python-essentials)
   - [Variables and Data Types](#variables-and-data-types)
   - [Control Flow](#control-flow)
   - [Functions](#functions)
   - [Classes and Objects](#classes-and-objects)
   - [Modules and Imports](#modules-and-imports)
   - [Exception Handling](#exception-handling)
2. [Coding Conventions (PEP 8)](#coding-conventions-pep-8)
   - [Naming Conventions](#naming-conventions)
   - [Indentation and Formatting](#indentation-and-formatting)
   - [Whitespace](#whitespace)
   - [Imports](#imports)
   - [Comments and Docstrings](#comments-and-docstrings)
   - [Best Practices](#best-practices)
   - [String Formatting](#string-formatting)
   - [Comparisons](#comparisons)
3. [Conclusion](#conclusion)

---

## Python Essentials

### Variables and Data Types

**Primitive Types:**
```python
# Numbers
age = 25              # int (whole number)
price = 19.99         # float (decimal)

# Text
name = "Alice"        # string

# Boolean
is_active = True      # True or False
empty = None          # represents "nothing"
```

**Collections:**
```python
# List - ordered, can change
fruits = ["apple", "banana", "cherry"]
fruits[0]             # "apple" (access by index)
fruits.append("date") # add item

# Tuple - ordered, can't change
point = (10, 20)
point[0]              # 10

# Dictionary - key-value pairs
person = {"name": "Bob", "age": 30}
person["name"]        # "Bob"
person["city"] = "NYC"  # add new

# Set - unique items only
numbers = {1, 2, 3, 3}  # becomes {1, 2, 3}
```

---

### Control Flow

**If Statements:**
```python
age = 20

if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teen")
else:
    print("Child")
```

**Loops:**
```python
# For loop - iterate over items
for fruit in ["apple", "banana"]:
    print(fruit)

for i in range(5):    # 0, 1, 2, 3, 4
    print(i)

# While loop - repeat while condition true
count = 0
while count < 5:
    print(count)
    count += 1

# Loop controls
for num in range(10):
    if num == 3:
        continue      # skip to next
    if num == 7:
        break         # exit loop
    print(num)
```

---

### Functions

```python
# Basic function
def greet(name):
    return f"Hello, {name}!"

result = greet("Alice")

# With default parameter
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Bob")          # "Hello, Bob!"
greet("Bob", "Hi")    # "Hi, Bob!"

# Multiple return values
def get_info():
    return "Alice", 25, "NYC"

name, age, city = get_info()

# Variable arguments
def sum_all(*numbers):
    return sum(numbers)

sum_all(1, 2, 3, 4)   # 10
```

---

### Classes and Objects

```python
# Define a class
class Dog:
    def __init__(self, name, age):
        self.name = name  # attribute
        self.age = age
    
    def bark(self):       # method
        return f"{self.name} says Woof!"

# Create object (instance)
my_dog = Dog("Buddy", 3)
print(my_dog.bark())      # "Buddy says Woof!"
print(my_dog.age)         # 3

# Inheritance
class Puppy(Dog):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed
    
    def bark(self):
        return f"{self.name} says Yip!"
```

---

### Modules and Imports

```python
# Import entire module
import math
result = math.sqrt(16)

# Import specific items
from math import sqrt, pi
result = sqrt(16)

# Import with alias
import pandas as pd
import numpy as np

# Import from your own file
# If you have mycode.py
from mycode import my_function
```

---

### Exception Handling

```python
# Basic try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Can't divide by zero!")

# Multiple exceptions
try:
    number = int("abc")
except ValueError:
    print("Not a valid number!")
except Exception as e:
    print(f"Error: {e}")

# With finally (always runs)
f = None
try:
    f = open("file.txt")
    data = f.read()
except FileNotFoundError:
    print("File not found")
finally:
    if f is not None:
        f.close()  # cleanup

# Better way with 'with'
with open("file.txt") as f:
    data = f.read()  # auto-closes
```

---

## Coding Conventions (PEP 8)

### Naming Conventions

```python
# Variables and functions: snake_case
user_name = "Alice"
total_count = 100

def calculate_total():
    pass

# Constants: UPPER_SNAKE_CASE
MAX_SIZE = 100
DEFAULT_TIMEOUT = 30

# Classes: PascalCase
class UserAccount:
    pass

class BankAccount:
    pass

# Private (internal use): prefix with _
class MyClass:
    def _internal_method(self):
        pass

# Good counter names
for i in range(10):     # i, j, k for loops
    pass

x, y = 10, 20           # x, y for coordinates
```

---

### Indentation and Formatting

```python
# Use 4 spaces (not tabs)
def my_function():
    if True:
        print("4 spaces per level")

# Keep lines under 79 characters
# Break long lines with parentheses
long_list = [
    "item1", "item2", "item3",
    "item4", "item5"
]

# Or with backslash
total = value1 + value2 + \
        value3 + value4

# 2 blank lines before functions/classes
def function_one():
    pass


def function_two():
    pass


# 1 blank line between methods
class MyClass:
    def method_one(self):
        pass
    
    def method_two(self):
        pass
```

---

### Whitespace

```python
# Spaces around operators
x = 5 + 3             # Good
x=5+3                 # Bad

y = x * 2
is_valid = x > 0 and y < 20

# Space after comma, not before
items = [1, 2, 3]     # Good
items = [1,2,3]       # Bad

# No spaces inside brackets
my_list[0]            # Good
my_list[ 0 ]          # Bad

# No space before function parentheses
greet("Alice")        # Good
greet ("Alice")       # Bad

# No space around = in keyword arguments
def func(default=5):  # Good
    pass

func(value=10)        # Good
```

---

### Imports

```python
# Each import on separate line
import os
import sys

# Group in order, with blank lines between:

# 1. Standard library
import os
import sys
from datetime import datetime

# 2. Third-party packages
import numpy as np
import pandas as pd

# 3. Your own modules
from myapp import mymodule

# Import specific items
from math import sqrt, pi

# Use alias for long names
import numpy as np

# Avoid wildcard imports
# from module import *  # Don't do this
```

---

### Comments and Docstrings

```python
# Single-line comments
x = x + 1  # Compensate for border

# Comment why, not what
x = x + 1  # Good: Adjust for offset
x = x + 1  # Bad: Increment x

# Function docstring
def calculate_area(radius):
    """
    Calculate the area of a circle.
    
    Args:
        radius: The circle radius
    
    Returns:
        The area of the circle
    """
    return 3.14159 * radius ** 2

# Class docstring
class Document:
    """
    Represent a document with title and content.
    
    Attributes:
        title: Document title
        content: Document content
    """
    def __init__(self, title):
        self.title = title
        self.content = ""
```

---

### Best Practices

```python
# 1. List comprehensions
squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]

# 2. Use 'with' for files
with open('file.txt') as f:
    data = f.read()

# 3. Explicit None checks
if value is not None:
    process(value)

# 4. Use enumerate for index + value
for i, item in enumerate(['a', 'b', 'c']):
    print(f"{i}: {item}")

# 5. Use zip for multiple lists
names = ['Alice', 'Bob']
ages = [25, 30]
for name, age in zip(names, ages):
    print(f"{name} is {age}")

# 6. isinstance() for type checking
if isinstance(value, str):
    print("It's a string")

# 7. Unpack sequences
first, *middle, last = [1, 2, 3, 4, 5]

# 8. Use any() and all()
has_positive = any(x > 0 for x in numbers)
all_positive = all(x > 0 for x in numbers)
```

---

### String Formatting

```python
name = "Alice"
age = 30
price = 19.99

# F-strings (preferred, Python 3.6+)
message = f"I'm {name}, {age} years old"
formatted = f"Price: ${price:.2f}"  # $19.99

# Expression in f-strings
result = f"Sum: {2 + 2}"
upper = f"Name: {name.upper()}"

# Multi-line f-strings
text = (
    f"Name: {name}\n"
    f"Age: {age}"
)

# Older methods (still valid)
message = "I'm {}, {} years old".format(name, age)
message = "I'm %(name)s" % {"name": name}
```

---

### Comparisons

```python
# Use 'is' for None, True, False
if x is None:
    pass

if x is not None:
    pass

# Use '==' for values
if x == 10:
    pass

if name == "Alice":
    pass

# Use 'in' for membership
if item in my_list:
    print("Found!")

if key in my_dict:
    value = my_dict[key]

# Chained comparisons
if 0 < x < 10:        # Pythonic
    pass

# Boolean checks
items = [1, 2, 3]
if items:             # Check if not empty
    process(items)

if not text:          # Check if empty
    print("Empty string")

# Simple boolean checks
if is_valid:          # Good
    pass

if is_valid == True:  # Bad - redundant
    pass
```

---

## Conclusion

**Key Takeaways:**

**Python Essentials:**
- Use appropriate data types (int, float, str, list, dict)
- Control flow with if/elif/else and for/while loops
- Functions help organize reusable code
- Classes group data and behavior together
- Handle errors with try/except
- Import modules to use existing code

**Coding Style (PEP 8):**
- `snake_case` for variables/functions
- `PascalCase` for classes
- `UPPER_CASE` for constants
- 4 spaces for indentation
- Spaces around operators
- Comment the "why", not the "what"
- Use f-strings for formatting
- Keep code readable and consistent

**Remember:** Code is read more than written. Focus on clarity over cleverness. Start simple, improve as you learn.

Practice these basics and you'll write clean, professional Python code! 🐍

---

## Contributed By:

**Author:** Siddharth Acharya  
**Program:** Computer Engineering, Himalaya College of Engineering  
**Email:** siddharthacharya258@gmail.com  
**Last Updated:** December 2025

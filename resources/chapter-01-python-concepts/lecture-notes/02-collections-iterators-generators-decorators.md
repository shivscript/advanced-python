# Advanced Data Structures in Python

---

## Overview

This guide covers essential Python concepts beyond basic lists and dictionaries. Learn to write cleaner and more efficient code for exams and projects.

**Prerequisites:** Basic Python (loops, functions, lists, dictionaries)

---

## 1. The `collections` Module

### 1.1 `Counter`

**What it does:**
- Automatically counts frequency of elements in any iterable
- Returns a dictionary-like object with elements as keys and counts as values
- Provides helpful methods like `most_common()` to find top elements

```python
from collections import Counter

votes = ['Alice', 'Bob', 'Alice', 'Alice', 'Bob']
result = Counter(votes)
print(result)  # Counter({'Alice': 3, 'Bob': 2})
print(result.most_common(1))  # [('Alice', 3)]
```

---

### 1.2 `defaultdict`

**What it does:**
- Eliminates KeyError by creating default values for missing keys
- Simplifies code by removing conditional checks before adding items
- Supports any default type: list, int, set, or custom functions

```python
from collections import defaultdict

students = defaultdict(list)
students['A'].append('Alish')
students['A'].append('Ram')
print(students)  # defaultdict(<class 'list'>, {'A': ['Alish', 'Ram']})
```

**Benefit:** No need to check if key exists before using it

---

### 1.3 `namedtuple`

**What it does:**
- Creates lightweight, immutable objects with named fields
- More readable than regular tuples (use names instead of indexes)
- Uses less memory than regular classes while providing similar functionality

```python
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(p.x)  # 10
print(p.y)  # 20
```

---

### 1.4 `deque`

**What it does:**
- Provides O(1) time complexity for adding/removing from both ends
- More efficient than lists for queue operations (lists are O(n) for front operations)
- Perfect for implementing stacks, queues, and sliding window algorithms

```python
from collections import deque

queue = deque([1, 2, 3])
queue.appendleft(0)  # Add to front: [0, 1, 2, 3]
queue.pop()          # Remove from end: [0, 1, 2]
print(queue)
```

**Use for:** Queues and stacks

---

## 2. Iterators

**What they do:**
- Process elements one at a time without loading entire dataset into memory
- Enable efficient looping over large files or infinite sequences
- Form the foundation for Python's for-loop mechanism

```python
numbers = [1, 2, 3]
it = iter(numbers)
print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
```

**Why useful:** Saves memory when working with large data

---

## 3. Generators

**What they do:**
- Create iterators using simple function syntax with `yield` keyword
- Generate values on-demand rather than storing everything in memory
- Can represent infinite sequences that would be impossible with lists

### Basic Example

```python
def count_up_to(n):
    for i in range(1, n + 1):
        yield i

for num in count_up_to(5):
    print(num)  # Prints 1, 2, 3, 4, 5
```

### Generator Expression

```python
squares = (x**2 for x in range(5))
print(next(squares))  # 0
print(next(squares))  # 1
```

**Advantage:** Uses less memory than creating a full list

---

## 4. Decorators

**What they do:**
- Modify or enhance function behavior without changing original code
- Enable code reuse by wrapping common functionality (logging, timing, etc.)
- Use simple `@decorator_name` syntax above function definitions

### Simple Example

```python
def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Before
# Hello!
# After
```

**Common uses:** Logging, timing, checking permissions

---

## 5. Quick Tips

### `functools.reduce`

**What it does:**
- Applies a function cumulatively to reduce sequence to single value
- Useful for operations like summing, finding products, or custom accumulation
- Takes two arguments at a time and carries result forward

```python
from functools import reduce

numbers = [1, 2, 3, 4]
total = reduce(lambda x, y: x + y, numbers)
print(total)  # 10
```

### Context Managers (`with` statement)

**What it does:**
- Guarantees proper resource cleanup (files, connections) even if errors occur
- Eliminates need for explicit close() calls and try-finally blocks
- Makes code cleaner and prevents resource leaks

```python
with open('file.txt') as f:
    data = f.read()
# File automatically closed here
```

---

## Quick Reference

| Feature | What It Does |
|---------|--------------|
| `Counter` | Counts occurrences |
| `defaultdict` | Auto-creates missing keys |
| `namedtuple` | Named tuple fields |
| `deque` | Fast queue/stack |
| Generators | Memory-efficient iteration |
| Decorators | Add behavior to functions |

---

## Key Takeaways

1. Use `Counter` to count things easily
2. Use `defaultdict` to avoid key checking
3. Use generators for large data
4. Use decorators to add functionality
5. Use `with` statement for files

---

## Contributed By:

**Author:** Alish Adhikari  
**Program:** Computer Engineering, Himalaya College of Engineering  
**Email:** [alishadhikari977@gmail.com](mailto:alishadhikari977@gmail.com)  
**Last Updated:** January 2026

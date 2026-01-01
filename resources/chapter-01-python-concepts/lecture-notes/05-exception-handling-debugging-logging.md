
## 🧠 Topic: Exception Handling, Debugging, and Logging

---

## 1️⃣ Exception Handling in Python

### 🔹 What is an Exception?
An **exception** is an error that occurs during the execution of a program and interrupts the normal flow of instructions.

Example:
```python
x = 10 / 0
```
This raises a `ZeroDivisionError`.

---

### 🔹 Need for Exception Handling
- Prevents program termination
- Handles runtime errors gracefully
- Improves program reliability
- Displays meaningful error messages

---

### 🔹 try–except Block
Used to handle exceptions.

```python
try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("Invalid input")
```

---

### 🔹 try–except–else
The `else` block runs if no exception occurs.

```python
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ZeroDivisionError:
    print("Division by zero")
else:
    print("Operation successful")
```

---

### 🔹 finally Block
Executes regardless of exception occurrence.

```python
try:
    file = open("data.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("File not found")
finally:
    print("Program ended")
```

---

### 🔹 Raising Exceptions
Custom exceptions can be raised using `raise`.

```python
age = int(input("Enter age: "))
if age < 18:
    raise ValueError("Age must be 18 or above")
```

---

### 🔹 Common Python Exceptions
- ZeroDivisionError
- ValueError
- TypeError
- IndexError
- KeyError
- FileNotFoundError

---

## 2️⃣ Debugging in Python

### 🔹 What is Debugging?
Debugging is the process of finding and fixing errors (bugs) in a program.

---

### 🔹 Types of Errors
1. **Syntax Error**
```python
if x > 5
    print(x)
```

2. **Runtime Error**
```python
print(10 / 0)
```

3. **Logical Error**
```python
print(2 + 2 * 2)  # Output: 6 (wrong logic)
```

---

### 🔹 Debugging Techniques
- Using print statements
- Reading traceback messages
- Using Python debugger (`pdb`)
- Testing code step by step

---

### 🔹 Debugging with print()
```python
x = 5
y = 0
print("x =", x)
print("y =", y)
print(x / y)
```

---

### 🔹 Using pdb (Python Debugger)
```python
import pdb
pdb.set_trace()

x = 10
y = 5
print(x / y)
```

Common Commands:
- `n` → next line
- `c` → continue
- `q` → quit
- `p var` → print variable

---

## 3️⃣ Logging in Python

### 🔹 What is Logging?
Logging is the process of recording messages during program execution to track events, warnings, and errors.

---

### 🔹 Advantages of Logging
- Better than print statements
- Saves output to files
- Supports severity levels
- Useful for debugging large programs

---

### 🔹 Logging Levels
| Level | Description |
|------|------------|
| DEBUG | Detailed information |
| INFO | General information |
| WARNING | Something unexpected |
| ERROR | Serious error |
| CRITICAL | System failure |

---

### 🔹 Basic Logging Example
```python
import logging

logging.basicConfig(level=logging.INFO)

logging.info("Program started")
logging.warning("Warning message")
logging.error("Error message")
```

---

### 🔹 Logging to a File
```python
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.debug("Debug message")
logging.info("Info message")
logging.error("Error message")
```

---

### 🔹 Logging with Exception Handling
```python
import logging

try:
    x = 10 / 0
except ZeroDivisionError:
    logging.error("Division by zero occurred")
```

---

## 📌 Summary
- Exception handling manages runtime errors using `try`, `except`, `else`, and `finally`.
- Debugging helps identify and fix syntax, runtime, and logical errors.
- Logging records program activities and errors for future analysis.

---



## Contributed By:

*Author:* Sujal Shrestha  
*Program:* Computer Engineering, Himalaya College of Engineering  
*Email:* sujalshrestha1470@gmail.com  
*Last Updated:* December 2025

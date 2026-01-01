# Working with Modules and Packages in Python

## Introduction
Python supports **modular programming**, which allows a program to be divided into smaller, reusable, and manageable components. This is achieved using **modules** and **packages**. Modular programming improves code organization, readability, reusability, and maintainability, especially in large applications.



## Modules in Python
A **module** is a single Python file (`.py`) that contains functions, classes, or variables. Modules allow related functionality to be grouped together and reused in multiple programs


### Purpose of Modules
- Break large programs into smaller files
- Avoid code duplication
- Improve readability and maintenance
- Enable reuse of code across programs


### Example of a User-Defined Module
**math_utils.py** #File definition
```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

### Importing the above mentioned user defined module
### Method 1 : Importing a Module
import math_utils
print(math_utils.add(10, 5))

### Method 2 : Importing Specific Members
from math_utils import subtract
print(subtract(10, 3))

### Method 3 : Importing with Alias
import math_utils as mu
print(mu.add(4, 6))

### Built-in Modules
Python provides several built-in modules that can be used without installation.
Example-
import math
print(math.sqrt(25))

Common built-in modules include:
math
random
sys
datetime




### Packages in Python
A package is a directory that contains multiple related modules. Packages help organize large programs into a hierarchical structure.

### Purpose of Packages
- Organize large projects
- Group related modules
- Avoid naming conflicts
- Support scalable applications

### Example Package Structure
mypackage/
├── __init__.py
├── module1.py
└── module2.py
Mypackage is a Package consisting of multiple modules here

### Creating Modules Inside a Package
module1.py
```python
def greet():
    print("Hello from module1")
```
module2.py
```python
def farewell():
    print("Goodbye from module2")
```

### Importing from a Package

### Method 1: Importing the Entire Module
from mypackage import module1
module1.greet()

### Method 2: Importing a Specific Function
from mypackage.module2 import farewell
farewell()




### The init.py File
The __init__.py file marks a directory as a Python package. It can also be used to control what is imported when the package is accessed.
Example
```python 
from .module1 import greet
```
Now the function can be imported directly:

```python
from mypackage import greet
```

### Absolute and Relative Imports
### Absolute Import
Uses the full path from the project root.
from mypackage.module1 import greet

### Relative Import
Uses dot (.) notation and is used inside packages.
from .module1 import greet

### External Packages and pip
External packages can be installed using the pip package manager.

Installing a Package
pip install numpy

Using the Installed Package
```python
import numpy as np
arr = np.array([1, 2, 3])
print(arr)
```

### Advantages of Modules and Packages
- Improved code structure
- Reusability of code
- Easier debugging and testing
- Better project organization
- Supports team collaboration

### Difference Between Module and Package 
***Module***
- A module is a single Python file with a .py extension.
- It contains functions, classes, and variables.
- Modules are used to divide a program into smaller reusable files.
- A module is suitable for small to medium-sized programs.
- It is imported using statements like import module_name.
- Example: math.py, random.py, user_defined.py.

***Package***
- A package is a directory that contains multiple Python modules.
- It is used to organize related modules together.
- Packages help manage large and complex projects.
- A package usually contains an __init__.py file.
- Modules inside a package are imported using dot (.) notation.
- Example: numpy, mypackage, django


# Object-Oriented Programming in Python

## Introduction

Object-Oriented Programming (OOP) is a programming paradigm that uses objects and classes to structure code in a modular, reusable, and organized way. Python is a versatile language that supports OOP principles alongside functional and procedural programming.

## Core Concepts

### Classes and Objects

A **class** is a blueprint for creating objects. It defines attributes (data) and methods (functions) that objects of that class will have. An **object** is an instance of a class.

```python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        return f"{self.name} says Woof!"

# Creating an object (instance)
my_dog = Dog("Buddy", 5)
print(my_dog.bark())  # Output: Buddy says Woof!
```

### Attributes and Methods

**Attributes** are variables that store data about an object. **Methods** are functions that define behaviors.

- **Instance attributes**: Unique to each object
- **Class attributes**: Shared by all instances of the class
- **Instance methods**: Operate on instance data
- **Class methods**: Operate on class data
- **Static methods**: Don't access instance or class data

```python
class Car:
    wheels = 4  # Class attribute
    
    def __init__(self, brand, model):
        self.brand = brand  # Instance attribute
        self.model = model
    
    def drive(self):  # Instance method
        return f"{self.brand} {self.model} is driving"
    
    @classmethod
    def from_string(cls, car_string):  # Class method
        brand, model = car_string.split("-")
        return cls(brand, model)
    
    @staticmethod
    def honk():  # Static method
        return "Honk! Honk!"

car1 = Car("Toyota", "Camry")
car2 = Car.from_string("Honda-Civic")
```

## Four Pillars of OOP

### 1. Encapsulation

Encapsulation is the bundling of data and methods into a single unit (class) and hiding internal details from the outside world.

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False
    
    def get_balance(self):  # Public method to access private data
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500
# account.__balance  # This would raise an AttributeError
```

### 2. Inheritance

Inheritance allows a class to inherit attributes and methods from another class, promoting code reuse.

```python
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return f"{self.name} makes a sound"

class Cat(Animal):
    def speak(self):  # Method overriding
        return f"{self.name} meows"

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks"

cat = Cat("Whiskers")
dog = Dog("Rex")
print(cat.speak())  # Output: Whiskers meows
print(dog.speak())  # Output: Rex barks
```

### 3. Polymorphism

Polymorphism allows objects of different classes to be treated through the same interface. It enables methods to take different forms.

```python
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print(shape.area())  # Polymorphism in action
```

### 4. Abstraction

Abstraction hides complex implementation details and exposes only necessary features. In Python, we use abstract base classes.

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        return "Car engine started"
    
    def stop(self):
        return "Car engine stopped"

# vehicle = Vehicle()  # Would raise TypeError
car = Car()
print(car.start())  # Output: Car engine started
```

## Special Methods (Dunder Methods)

Special methods allow you to define how objects interact with Python's built-in functions and operators.

```python
class MiniFrame:
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return f"<MiniFrame: {len(self.data)} rows>"

    def __getitem__(self, idx):
        return self.data[idx]
```

## Class Inheritance Patterns

### Single Inheritance

```python
class Parent:
    pass

class Child(Parent):
    pass
```

### Multiple Inheritance

```python
class Mixin1:
    pass

class Mixin2:
    pass

class Child(Mixin1, Mixin2):
    pass
```

### Multi-level Inheritance

```python
class Grandparent:
    pass

class Parent(Grandparent):
    pass

class Child(Parent):
    pass
```

## Practical Example: Complete OOP Application

```python
class Employee:
    company_name = "Tech Corp"
    employee_count = 0
    
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
        Employee.employee_count += 1
    
    def give_raise(self, amount):
        self.salary += amount
        return f"{self.name}'s new salary: ${self.salary}"
    
    def __str__(self):
        return f"{self.name} - {self.position} (${self.salary})"
    
    @classmethod
    def get_employee_count(cls):
        return f"Total employees: {cls.employee_count}"

class Manager(Employee):
    def __init__(self, name, position, salary, department):
        super().__init__(name, position, salary)
        self.department = department
    
    def __str__(self):
        return f"{super().__str__()} - Department: {self.department}"

emp1 = Employee("Alice", "Developer", 70000)
emp2 = Manager("Bob", "Manager", 90000, "Engineering")

print(emp1)  # Output: Alice - Developer ($70000)
print(emp2)  # Output: Bob - Manager ($90000) - Department: Engineering
print(Employee.get_employee_count())  # Output: Total employees: 2
```

## Best Practices

1. **Use meaningful class and method names** that clearly describe their purpose
2. **Follow the Single Responsibility Principle**: Each class should have one reason to change
3. **Prefer composition over inheritance** when appropriate to avoid deep hierarchies
4. **Use private attributes** (prefix with `_` or `__`) to protect internal state
5. **Document your classes** with docstrings explaining purpose and usage
6. **Keep methods focused and concise**, following the DRY principle
7. **Avoid deep inheritance chains** that become difficult to understand and maintain
8. **Use properties** for controlled access to attributes

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius
    
    @property
    def fahrenheit(self):
        """Convert celsius to fahrenheit"""
        return (self._celsius * 9/5) + 32
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero")
        self._celsius = value

temp = Temperature(25)
print(temp.fahrenheit)  # Output: 77.0
```
## Final Challenge – Pipeline

```python
import math

class Pipeline:
    def __init__(self):
        self.steps = []

    def add(self, step):
        self.steps.append(step)

    def run(self, data):
        current = data
        for step in self.steps:
            step.fit(current)
            current = step.transform(current)
        return current


class LogTransformer:
    def fit(self, data):
        pass

    def transform(self, data):
        return [math.log(x) for x in data]
```


## Contributed By:

**Author: Sushant Gautam**

**Program: Computer Engineering, Himalaya College of Engineering**

**Email: sushant98677@gmail.com**

**Last Updated: January 2026**

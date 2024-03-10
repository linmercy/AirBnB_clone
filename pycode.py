#!/usr/bin/python3
"""This module defines a simple class."""

class MyClass:
    """A simple class with a constructor and a method."""

    def __init__(self, name):
        """Initialize the instance with a name."""
        self.name = name

    def greet(self):
        """Print a greeting message."""
        print(f"Hello, {self.name}!")

# Instantiate the class
obj = MyClass("Alice")

# Call the method
obj.greet()


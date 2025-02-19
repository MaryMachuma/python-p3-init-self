#!/usr/bin/env python3

class Person:
    def __init__(self, name):
        self.name = name

# Test the class by creating an instance
if __name__ == "__main__":
    sophie = Person("Sophie")
    print(f"Person's name is {sophie.name}.") # Expected: Person's nsme is Sophie

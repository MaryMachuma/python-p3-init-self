#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed

# Test the class by creating instances (should be outside the class)
if __name__ == "__main__":
    fido = Dog("Fido")
    snoopy = Dog("Snoopy", "Beagle")

    print(f"{fido.name} is a {fido.breed}.")  # Expected: Fido is a Mutt.
    print(f"{snoopy.name} is a {snoopy.breed}.")  # Expected: Snoopy is a Beagle.

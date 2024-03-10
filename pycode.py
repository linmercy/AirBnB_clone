import os
import sys


def greet(name):
    """Greet a person by name."""
    print("Hello, {}!".format(name))


def main():
    """Main function."""
    name = input("Enter your name: ")
    greet(name)


if __name__ == "__main__":
    main()

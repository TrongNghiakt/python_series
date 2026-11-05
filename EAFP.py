# Duck Typing and Asking Forgiveness, Not Permission (EAFP)

import os


class Duck:
    def quack(self):
        print("Quack, quack!")

    def fly(self):
        print("Flap, flap!")


class Person:
    def quack(self):
        print("I'm quacking like a duck!")

    def fly(self):
        print("I'm flapping my arms and pretending to fly!")


def quack_and_fly(thing):
    # Not Duck-Typed (Non-Pythonic)
    # if isinstance(thing, Duck):
    #     thing.quack()
    #     thing.fly()
    # else:
    #     print('This has to be a Duck!')

    # LBYL (Non-Pythonic)
    # LBYL = Look Before You Leap.
    # if hasattr(thing, 'quack'):
    #     if callable(thing.quack):
    #         thing.quack()

    # if hasattr(thing, 'fly'):
    #     if callable(thing.fly):
    #         thing.fly()

    # EAFP (Pythonic)
    # EAFP = Easier to Ask Forgiveness than Permission.
    try:
        thing.quack()
        thing.fly()
        # This will raise an AttributeError since Person doesn't have a bark method.
        thing.bark()
    except AttributeError as e:
        print(e)
    print()


d = Duck()
quack_and_fly(d)

p = Person()
quack_and_fly(p)


# person = {'name': 'Jess', 'age': 23, 'job': 'programmer'}
person = {'name': 'Jess', 'age': 23}

# LBYL (Non-Pythonic)
if 'name' in person and 'age' in person and 'job' in person:
    print("I'm {name}. I'm {age} years old and I am a {job}".format(**person))
else:
    print("Missing some keys!")

print()


# EAFP (Pythonic)
try:
    print("I'm {name}. I'm {age} years old and I am a {job}".format(**person))
except KeyError as e:
    print(f"Missing key: {e}")


my_list = [1, 2, 3, 4, 5]

# Non-Pythonic
if len(my_list) >= 6:
    print(my_list[5])
else:
    print("That index doesn't exist!")

print()

# Pythonic
try:
    print(my_list[5])
except IndexError as e:
    print(f"That index doesn't exist! {e}")


# Example from the Python Docs

my_file = "D:\\python_learning\\csv\\test0.txt"

# Race Condition
if os.access(my_file, os.R_OK):
    with open(my_file) as f:
        print(f.read())
else:
    print("The file is not accessible!")

print()

# No Race-Condition
try:
    f = open(my_file)
except OSError as e:
    print(f"The file is not accessible!")
else:
    with f:
        print(f.read())

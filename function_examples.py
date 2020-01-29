#!/usr/bin/env python
from typing import Union, Iterable

def get_message() -> str:
    return "Hello, world"

def say_hello():
    message = get_message()
    print(message)

m = get_message()
print(m)

say_hello()

x = say_hello()
print(x)
print(type(x))


def doomed():
    raise ValueError("You are not happy")

try:
    doomed()
except ValueError as err:
    print(err)

print(say_hello(), say_hello)

x = say_hello


say_hello()

a = 5   # bind 'a' to integer obj
b = a   # bind 'b' to same obj as 'a'
a = 10
print(b)

p = [1, 2, 3]
r = p
r.append('wombat')
print(p)

s = list(p)
s.append("weaselbreath")

print(p)
print(s)

def greet(whom):
    print("Hello,", whom)

greet("world")
greet("Mom")
greet(234)
greet([1,2,3,4])
greet(greet)

def forced_greet(whom):
    if isinstance(whom, str):
        print("hello,", whom)
    else:
        raise TypeError("whom must be a str")


def hinted_greet(whom: str) -> None:
    print("hello,", whom)

hinted_greet("mom")
hinted_greet(123)

AnyNumber = Union[int, float]

def double(x: AnyNumber) -> AnyNumber:
    return x * 2


def process_filenames(file_names: Iterable[str]):
    pass


name = "Bob"
print(name, type(name), id(name))

# PHP
#  == ===

# Python
# == is
#  id(foo) == id(bar)
#  foo is bar
#  foo == bar


def spam(x, y=100):
    print(x, y)


spam('a', 'b')
spam("wombat")
print()

# def open(file_name, mode="r"):
#     pass
#
# with open("foo.txt") as foo_in:
#     pass
#
# with open("bar.txt", "w") as bar_out:
#     pass

def multi_greet(greeting, *people):
    print(people)
    for person in people:
        print(f"{greeting}, {person}")
    print("----")


multi_greet("hello", "world")

multi_greet("howdy", "Mom", "Dad", "sis", "Aunt Betty")

multi_greet("hiya")

def get_config(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k, v)
    print("====")


get_config(animal="wombat", city="Sophia", country="Latvia")


def wacky(p1, p2, *p3, x, y, **p4):
    pass


import lxml.etree as ET

e = ET.Element('spam', color="black", country="Myanmar")

print(ET.tostring(e, pretty_print=True).decode())


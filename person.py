from dataclasses import dataclass


@dataclass
class Person:
    first_name: str
    last_name: str
    age: int

if __name__ == '__main__':
    p1 = Person("Joe", "Schmoe", 42)
    print(p1.first_name, p1.last_name)

    p1.last_name = 'Smith'

    print(p1)

    p2 = Person("Joe", "Smith", 42)

    print(p1 == p2)
    print(p1 is p2)

    p1.last_name = 1234

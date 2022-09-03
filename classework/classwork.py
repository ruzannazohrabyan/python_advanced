class Person:
    no_of_ears = 2

    def __init__(self, name, age):
        self.name = name
        self.age = age


person1 = Person("Ruzanna", 21)
person2 = Person("Hasmik", 9)

person1.no_of_ears = 1

print(person1)
print(person2)


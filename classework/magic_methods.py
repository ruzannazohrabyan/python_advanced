class Employee:
    def __new__(cls):
        print("__new__ magic method is called")
        inst = object.__new__(cls)
        return inst

    def __init__(self):
        print("__init__ magic method is called")
        self.name = 'Satya'


employee1 = Employee()


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return self.area() + other
        return self.area() + other.area()

    def __radd__(self, other):
        return self.__add__(other)


# rect = Rectangle(10, 20)
# rect1 = Rectangle(20, 30)
# rect2 = Rectangle(30, 40)
# sum = rect + rect1 + rect2
# print(sum)


class Building:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors
        self.occupants = [None] * 3

    def __setitem__(self, key, value):
        self.occupants[key] = value

    def __getitem__(self, item):
        return self.occupants[item]

    def __len__(self):
        return self.floors


# building1 = Building("Empire State", 3)
#
# building1[0] = "My room"
#
# print(building1[0])

class Foo:
    def __init__(self, x):
        self.x = x

    # def __setattr__(self, key, value):


a = Foo(42)

# a.y =
print(a.x)

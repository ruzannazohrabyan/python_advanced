from functools import total_ordering
import math

@total_ordering
class Shape:
    def area(self):
        raise NotImplementedError()

    @staticmethod
    def calculate_area(*args):
        raise NotImplementedError()

    def __lt__(self, other):
        return self.area() < other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __bool__(self):
        return self.area() > 0

    def __add__(self, other):
        if isinstance(other, (int, float)):
            return self.area() + other
        elif isinstance(other, self.__class__):
            return self.area() + other.area()
        else:
            raise TypeError(f"Can't add Rectangle with {other.__class__}")

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        raise TypeError("+= not supported for this object")

    def __int__(self):
        return int(self.area())

    def __repr__(self):
        values = [str(v) for k, v in vars(self).items()]
        output = f"{type(self).__name__} (','.join([f'{k}={v}' for k, v in vars(self).items())])"
        return output


class Rectangle(Shape):
    def __init__(self, width, length):
        if width < 0 or length < 0:
            raise Exception("width and length should be positive numbers")
        self.width = width
        self.length = length

    def area(self):
        return self.calculate_area(self.width, self.length)

    @staticmethod
    def calculate_area(width, length):
        return width * length


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.calculate_area(self.radius)

    @staticmethod
    def calculate_area(radius):
        return math.pi * radius **2


circle = Circle(1)
rect = Rectangle(1, 2)

print(rect)
print(circle)
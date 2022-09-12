from datetime import date
from enum import Enum


class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        values = [f"{key}={value}" for key, value in vars(self).items()]
        output = f"{self.__class__.__name__}({', '.join(values)})"
        return output


class Student(Person):

    def __init__(self, name, date_of_birth, student_class, subjects=None):
        super().__init__(name)
        self.date_of_birth = date.fromisoformat(date_of_birth)
        self.student_class = student_class
        self.subjects = {}
        self.assign_subject(subjects)

    def assign_subject(self, subjects):
        if isinstance(subjects, Enum):
            if subjects.name not in self.subjects.keys():
                self.subjects[subjects.name] = None
        elif subjects is not None:
            for item in subjects:
                if item.name not in self.subjects.keys():
                    self.subjects[item.name] = None

    @property
    def age(self):
        return date.today().year - self.date_of_birth.year


class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def grading(self, student, point):
        if self.subject.name in student.subjects:
            student.subjects[self.subject.name] = point
        else:
            raise TypeError("You cannot grade this student!")

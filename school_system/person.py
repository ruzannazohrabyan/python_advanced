from datetime import date
from enum import Enum


class Person:
    def __init__(self, name):
        self.name = name

    # def __repr__(self):
    #     values = [f"{key}={value}" for key, value in vars(self).items()]
    #     output = f"{self.__class__.__name__}({','.join(values)})"
    #     return output


class Student(Person):

    def __init__(self, name, date_of_birth, clazz, subjects=None):
        super(Student, self).__init__(name)
        self.date_of_birth = date.fromisoformat(date_of_birth)
        self.clazz = clazz
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


class Teacher(Person):
    def __init__(self, name, subject):
        super(Teacher, self).__init__(name)
        self.subject = subject

    def grading(self, student, point):
        if self.subject.name in student.subjects:
            student.subjects[self.subject.name] = point
        else:
            raise TypeError("You cannot grade this student!")

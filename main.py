from school_system import Subjects
from school_system import Teacher, Student

if __name__ == "__main__":
    first_class_subjects = [Subjects.MATH, Subjects.ENGLISH]
    second_class_subjects = [Subjects.HISTORY, Subjects.MATH, Subjects.BIOLOGY]

    teacher1 = Teacher("Ruzanna", Subjects.BIOLOGY)
    teacher2 = Teacher("Karen", Subjects.MATH)

    # Birthdate should be in this format: YYYY-MM-DD
    student1 = Student("Eric", "2010-08-10", 1, first_class_subjects)
    student2 = Student("Hasmik", "2013-10-09", 2)
    student2.assign_subject(second_class_subjects)

    print(student1)
    print(teacher1)
    print(student1.subjects)
    print(student2.subjects)
    teacher1.grading(student2, 7)
    teacher2.grading(student1, 10)
    print("After grading")
    print(student1.subjects)
    print(student2.subjects)
    print(student1.age)
    # Here should throw an exception, because teacher1 unable to grade student1
    # teacher1.grading(student1, 10)


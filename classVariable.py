class Student:

    class_year = 2025
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

    def displayStudent(self):
        print(f"Student name: {self.name}, Age: {self.age}, Year: {Student.class_year}")

v = Student('Kiran', 12)
v.displayStudent()
print(f"Year {Student.class_year} has {Student.num_students} student(s).")

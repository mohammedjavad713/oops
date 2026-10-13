# Create a program to store a student's name, age, and course and display the student's details

class Student:
    def __init__(self , name,age,course):
        self.name = name
        self.age = age
        self.course = course

s1 = Student("Anu", 20, "Computer Science")
s2 = Student("abhinand",22,"cs")

print("student name: ",s2.name)
print("student age: ",s1.age)
print("student course: ",s1.course)
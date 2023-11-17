class Student:
    def __init__(self, name, year, course, grades):
        self.name = name
        self.year = year
        self.course = course
        self.grades = grades

    def __str__(self):
        return f"Name: {self.name}, Year: {self.year}, Course: {self.course}, Grades: {self.grades}"


student = {
    "James Hunt": Student("James Hunt", "29-08-2005", 2, 60),
    "Niki Lauda": Student("Niki Lauda", "22-02-2006", 1, 81),
    "Matias Lauda": Student("Matias Lauda", "30-01-2005", 2, 74),
}
new_student = Student("John Doe", "01-01-2003", 4, 85)
student["John Doe"] = new_student

print(student.keys())
print()

student["Niki Lauda"] = Student("Niki Lauda", "22-02-2001", 1, 90)
for i in student.values():
    print(i)
print()

student["James Hunt"].grades = 75
student.pop("Niki Lauda")

print(student.get("James Hunt"))
print()

print(student.keys())
print()

for i in student.values():
    print(i)
print()
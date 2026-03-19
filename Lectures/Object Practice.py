class Student:
    def __init__(self, name, age, school, major):
        self.name = name
        self.age = age
        self.school = school
        self.major = major
    def isAwake(self):
        isAwake = True
        if "Chemistry" in self.major:
            isAwake = False
        return isAwake
student1 = Student("Matthew",20,"BYU","Computer Science")
student2 = Student("James", 24, "BYU", "Chemistry")
print(f"{student1.name} is awake? {student1.isAwake()}")
print(f"{student2.name} is awake? {student2.isAwake()}")
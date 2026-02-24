class Student:
    school_name = "High School #1"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school_name(cls, new_name):
        cls.school_name = new_name


print("Before:", Student.school_name)
Student.change_school_name("International School")
print("After:", Student.school_name)
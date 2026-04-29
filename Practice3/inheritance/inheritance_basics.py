#1
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


x = Person("John", "Doe")
x.printname()

#2
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    pass

x = Student("Mike", "Olsen")
x.printname()

#3
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

x = Student("Mike", "Olsen")
x.printname()

#4
class Animal():
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Animal makes sound"
    
class Dog(Animal):
    def bark(self):
        return "WOOF!"
    
dog1 = Dog("Aktos")
print(dog1.name)
print(dog1.speak())
print(dog1.bark())

#5
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major

    def info(self):
        return f"Student name: {self.name} \nStudent age: {self.age} \nStudent major: {self.major}"
    
name = "Madina"
age = 17
major = "Information system"
studentinfo = Student(name, age, major)
print(studentinfo.info())
#1
class uni():
    uni_name = "KBTU"

    def __init__(self, name):
        self.name = name

name = "Madina"
p1 = uni(name)
print(p1.uni_name)

#2
class Employee():
    raise_rate = 1.1

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def apply_salary(self):
        return f"{self.name}: {int(self.salary * Employee.raise_rate)}"
    
name = "Madina"
salary = 1700000
p = Employee(name, salary)
print(p.apply_salary())

#3
class GameSettings():
    max_player = 4
    difficulty ="normal"

    def __init__(self, player_name):
        self.player_name = player_name

p1 = GameSettings("Madina")
p2 = GameSettings("Ali")
p3 = GameSettings("Aruzhan")
print(p1.difficulty)
print(p2.difficulty)
print(p3.difficulty)
GameSettings.difficulty = "hard"
print(p1.difficulty)
print(p2.difficulty)
print(p3.difficulty)

#4
class LibraryBooks():
    total_books = 0

    def __init__(self, title):
        self.title = title
        LibraryBooks.total_books += 1

    @classmethod
    def get_total(cls):
        return cls.total_books
    
p = LibraryBooks("Abay joly")
p1 = LibraryBooks("Gauhartas")

print(p.get_total())

#5
class Logger():
    logs = []

    def __init__(self, message):
        self.message = message
        Logger.logs.append(message)

    @classmethod
    def show_logs(cls):
        return Logger.logs
    
l1 = Logger("User logged in")
l2 = Logger("File uploaded")

print(Logger.show_logs())
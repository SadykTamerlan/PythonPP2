class Employee:
    company_name = "Tech Company"

    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Employee: {self.name}, Company: {Employee.company_name}")


emp1 = Employee("Tamerlan")
emp1.display()
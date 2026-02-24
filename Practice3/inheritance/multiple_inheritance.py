class Father:
    def skills(self):
        print("Father: Driving")


class Mother:
    def skills(self):
        print("Mother: Cooking")


class Child(Father, Mother):
    pass


child = Child()
child.skills()  # Uses Father class method due to MRO
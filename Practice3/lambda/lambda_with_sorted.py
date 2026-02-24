
students = [
    {"name": "Ali", "grade": 85},
    {"name": "Dana", "grade": 92},
    {"name": "Nursultan", "grade": 78}
]

sorted_students = sorted(students, key=lambda student: student["grade"])

print("Students sorted by grade:")
for student in sorted_students:
    print(student)
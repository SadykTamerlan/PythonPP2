def square(number):
    """Returns square of a number"""
    return number ** 2


def get_full_name(first_name, last_name):
    """Returns full name"""
    return f"{first_name} {last_name}"


result = square(6)
print("Square:", result)

full_name = get_full_name("Tamerlan", "Sadyk")
print("Full Name:", full_name)
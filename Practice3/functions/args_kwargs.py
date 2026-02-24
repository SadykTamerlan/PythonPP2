def sum_all(*args):
    """Accepts any number of positional arguments"""
    return sum(args)


def print_user_info(**kwargs):
    """Accepts any number of keyword arguments"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# Function calls
print("Sum:", sum_all(1, 2, 3, 4, 5))

print_user_info(name="Tamerlan", age=20, city="Almaty")
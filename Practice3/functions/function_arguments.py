def describe_pet(pet_name, animal_type="dog"):
    """Default argument example"""
    print(f"I have a {animal_type} named {pet_name}.")


def calculate_total(price, quantity):
    """Positional arguments example"""
    total = price * quantity
    print("Total price:", total)


describe_pet("Buddy")
describe_pet("Milo", "cat")

calculate_total(100, 3)
calculate_total(price=50, quantity=4)
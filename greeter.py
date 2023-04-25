def greet_user(username):
    """Display a simple greeting"""
    print(f"Hello!, {username.title()}!")

greet_user("alex")

def display_message(name):
    """Display a message"""
    print(f"I, {name.title()} am learning python")

display_message("alex")

def favorite_book(title):
    """Displaying my favorite book"""
    print(f"My favorite book is {title.title()}")

favorite_book("Lord of the rings")

def describe_pet(animal_type, pet_name):
    """Display info about a pet"""
    print(f"\ni have a {animal_type}.")
    print(f"{pet_name} is a {animal_type}")

describe_pet('hamster','harry')
describe_pet('dog','willie')
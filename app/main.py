class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:  # Added return type annotation
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        Person.people[name] = self


def create_person_list(people: list) -> list:  # Ensured two blank lines before function
    # First pass: create all Person instances
    persons = [Person(person["name"], person["age"]) for person in people]  # Replaced single quotes

    # Second pass: assign relationships
    for person in people:
        person_instance = Person.people[person["name"]]  # Replaced single quotes
        if "wife" in person and person["wife"]:  # Replaced single quotes
            person_instance.wife = Person.people[person["wife"]]  # Replaced single quotes
        elif "husband" in person and person["husband"]:  # Replaced single quotes
            person_instance.husband = Person.people[person["husband"]]  # Replaced single quotes

    return persons

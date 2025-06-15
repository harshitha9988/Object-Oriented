class Dog:
    species = "Canis familiaris"
    
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Breed: {self.breed}")
        print(f"Species: {Dog.species}")
        print("-" * 20)

d1 = Dog("Buddy", "Golden Retriever")
d2 = Dog("Max", "German Shepherd")

d1.display_details()
d2.display_details()
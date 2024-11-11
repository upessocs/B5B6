from animal import Animal
class Dog(Animal):
    species = "Canis familiaris"
    
    def bark(self):
        return f"{self.name} says woof!"
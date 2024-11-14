from animal import Animal
class Cat(Animal):
    species = "Cat Species"
    
    def meu(self):
        return f"{self.name} says meu!"
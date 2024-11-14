class Dog:
        # Class attribute (shared by all instances)
    species = "Canis familiaris"
    
    # Constructor (initializer)
    def __init__(self, name, age):
        # Instance attributes (unique to each instance)
        self.name = name
        self.age = age
    
    # Instance method
    def bark(self):
        return f"{self.name} says woof!"
    
    # Another instance method
    def get_age(self):
        return f"{self.name} is {self.age} years old."


class Cat:
        # Class attribute (shared by all instances)
    species = "Cat Species"
    
    # Constructor (initializer)
    def __init__(self, name, age):
        # Instance attributes (unique to each instance)
        self.name = name
        self.age = age
    
    # Instance method
    def meu(self):
        return f"{self.name} says meu!"
    
    # Another instance method
    def get_age(self):
        return f"{self.name} is {self.age} years old."


cat1 = Cat("cat1Name",3)
cat2 = Cat("cat2Name",5)


dog1 = Dog("dog1Name",3)
dog2 = Dog("dog2Name",5)


dog1.bark()
dog2.get_age()

print(dog1.bark())         # Buddy says woof!
print(dog2.get_age())      # Charlie is 5 years old.
print(dog1.species)        # Canis familiaris

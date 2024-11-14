
from dog import Dog
from cat import Cat
    
    


    
    
cat1 = Cat("cat1Name",3)
cat2 = Cat("cat2Name",5)


dog1 = Dog("dog1Name",3)
dog2 = Dog("dog2Name",5)


dog1.bark()
dog2.get_age()

print(dog1.bark())         # Buddy says woof!
print(dog2.get_age())      # Charlie is 5 years old.
print(dog1.species)        # Canis familiaris

print(dog1.age)
print(dog1)


# init repr str getter and setters,



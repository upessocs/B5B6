class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.__age = age #private
    
    def get_age(self):
        return f"{self.name} is {self.__age} years old."
    
    def __str__(self):
        return f"this is \n {self.name} \n its age is {self.age}"
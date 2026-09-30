print("------------------------Extra Exercise 2-------------------------")
class Animal :
    def __init__(self, name: str):
        self.name = name

    def speak(self):
        return "Hace un sonido"
    
class Dog (Animal):
    def speak (self):
        return "Guau"

class Cat (Animal):
    def speak (self):
        return "Miau"


dog = Dog ("firulais")
cat = Cat ("Minino")

animal = Animal ("Animal Misterioso")

print (f"{animal.name} dice: {animal.speak()}")
print (f"{dog.name} dice: {dog.speak()}")
print (f"{cat.name} dice: {cat.speak()}")
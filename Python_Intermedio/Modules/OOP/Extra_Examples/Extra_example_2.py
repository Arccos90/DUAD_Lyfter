class Animal:
    def __init__(self, nombre: str):
        self.nombre = nombre

    def dormir(self):
        print(f"{self.nombre} está durmiendo... zzz")

# Clases Hijas (heredan de Animal poniendo el padre entre paréntesis)
class Perro(Animal):
    def ladrar(self):
        print(f"{self.nombre} dice: ¡Guau!")

class Gato(Animal):
    def maullar(self):
        print(f"{self.nombre} dice: ¡Miau!")

firulais = Perro ("Firu")
michi = Gato("Michi")

print(f"que esta haciendo el gato?")
michi.dormir()
michi.maullar()
"--------------------Exercise_3: Research about multiple inheritance-------------"
# Entendí que la herencia múltiple permite asignar ciertas habilidades temporales a un objeto. 
# A esto se le llama mixins, esas pequenas clases solo tienen habilidades muy especificas. 
# La analogía que encontré habla de un guerrero de un video juego y que se le agregan "alas" o "aletas", estas serian esas habilidades.

class Vehicle:
    def __init__(self, name:str):
        self.name = name
class NavigateMixin :
    def navegar (self):
        print(f"{self.name}, Puede navegar por el agua!")

class WheelerMixin :
    def rodar (self):
        print(f"{self.name}, Puede transitar por la tierra!")

class Boat (Vehicle, NavigateMixin):
    pass

class Car (Vehicle, WheelerMixin):
    pass

class Anfibio (Vehicle, NavigateMixin, WheelerMixin):
    pass
    


name = str(input("Ingrese el Nombre del Vehiculo: "))
type = int(input("¿ Que tipo de vehiculo es? 1-Maritimo / 2-Terrestre / 3-Anfibio: "))

if type == 1:
    vehicle = Boat(name)
    vehicle.navegar()

elif type == 2:
    vehicle = Car(name)
    vehicle.rodar()
elif type == 3:
    vehicle = Anfibio(name)
    vehicle.navegar()
    vehicle.rodar()
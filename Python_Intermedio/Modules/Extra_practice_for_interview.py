class Vehiculo:
    def encender(self):
        print("Vehículo encendido")

class Computadora:
    def encender(self):
        print("Computadora encendida cargando Windows")

objetos = [Vehiculo(), Computadora()]
for obj in objetos:
    obj.encender() # Polimorfismo en acci
class Car:
    wheel_number = 4
    gas_type = "diesel"
    def my_first_method(self):
        print("hello OPP")
    def show_history (self, miles, crashes):
        print(f"this car has {miles} miles, and {crashes} crashes and {self.wheel_number} wheels")
    def upgrade_engine (self):
        if self.gas_type == "diesel":
            print("Cambiando el motor diesel por uno de gasolina super por $1200...")
            self.gas_type = "super"
        else:
            print("Ya tiene un motor de gasolina super")


print("Prueba.......")
print("Vehiculo de Fabrica")
my_car = Car()
my_car.my_first_method()
my_car.show_history(1000,5)
my_car.upgrade_engine()
print("Vehiculo modificado")
my_car.upgrade_engine()

print("Vehiculo 2....")
my_car_2 = Car()
my_car_2.gas_type="super"
my_car_2.show_history(2500,8)
my_car_2.upgrade_engine()
my_car_2.wheel_number=8
my_car_2.show_history(2500,8)

print(my_car.wheel_number)
print(my_car_2.wheel_number)
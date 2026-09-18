class Bus:

    def __init__(self, passenger_capacity_in_kg ):
        self.passengers = []
        self.current_weight =0
        self.counter=0
        self.max_passenger = passenger_capacity_in_kg 
    def accept_passenger(self, name, weight):
        if self.current_weight + weight <= self.max_passenger:
                self.passengers.append({'name': name, 'weight':weight})
                self.current_weight += weight
                self.counter += 1
                return True
        else:
            print("""-------------------------------------
                     The bus is full
                     -------------------------------------
                     """)
            return False
        
    def let_passenger_off(self,name):
        for i, passenger in enumerate(self.passengers):
            if passenger['name'].lower() == name.lower():
                removed_passenger = self.passengers.pop(i)
                self.current_weight-= removed_passenger['weight']
                self.counter -= 1
                print(f"\n {removed_passenger['name']} ha bajado del bus.")
                return True
              
        print (f"El pasajero '{name}' no se encuentra en el bus")
        return False

         
bus_capacity = int(input(f"Ingrese la capacidad del bus:"))
bus_1 = Bus(bus_capacity)
while True:
    name=input(f"Ingrese el nombre del pasajero o salir para terminar:").strip()
    if name.lower() == "salir": 
            break
    weight=int(input(f"Ingrese el peso del pasajero:"))
    subio = bus_1.accept_passenger(name, weight)
    if subio:
        ultimo=bus_1.passengers[-1]
        available_capacity = bus_1.max_passenger - bus_1.current_weight
        print(f"Pasajero {bus_1.counter}: {ultimo['name']} -- {ultimo['weight']}kg")
        print(f"Peso Actual: {bus_1.current_weight}kg")
        print(f"Capacidad Disponible: {available_capacity}kg")
    else:
         decision = input("Desea bajar un pasajero? (s/n)").strip().lower()
         if decision == 's':
            person_getting_off = input("Ingrese el nombre del pasajero que se bajará:").strip()
            bus_1.let_passenger_off(person_getting_off)
            print(f"Capacidad actual del bus: {bus_1.max_passenger - bus_1.current_weight}kg")
            for i, p in enumerate (bus_1.passengers, start =1):
                    print(f"{i}. Nombre: {p['name']} .... Peso: {p['weight']}kg")
            print(f"Total de personas en el bus: {bus_1.counter}")
            print(f"Ocupacion actual: {(bus_1.current_weight / bus_1.max_passenger)*100} %")
print("""
---------------------------Lista Final de Pasajeros----------------------------------

""")
if not bus_1.passengers:
     print("El bus esta vacío")
else:
    for i, p in enumerate (bus_1.passengers, start =1):
        print(f"{i}. Nombre: {p['name']} .... Peso: {p['weight']}kg")
    print(f"Total de personas en el bus: {bus_1.counter}")
    print(f"Peso total: {(bus_1.current_weight / bus_1.max_passenger)*100} %")
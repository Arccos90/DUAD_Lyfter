class Person:
    def __init__(self, name:str):
         self.name = name

class Bus:
    def __init__(self, max_passenger: int ):
        self.passengers = []
        self.counter=0
        self.max_passenger = max_passenger
    def accept_passenger(self, person:Person):
        if len (self.passengers) < self.max_passenger:
                self.passengers.append(person)
                self.counter += 1
                print(f"{person.name} ha subido al bus")
                return True
        else:
            print("""-------------------------------------
                     The bus is full
                     -------------------------------------
                     """)
            return False
        
    def let_passenger_off(self,name:str):
        for i, passenger in enumerate(self.passengers):
            if passenger.name.lower() == name.strip().lower():
                removed_passenger = self.passengers.pop(i)
                self.counter -= 1
                print(f"\n {removed_passenger.name} ha bajado del bus.")
                return True
              
        print (f"El pasajero '{name}' no se encuentra en el bus")
        return False

         
bus_capacity = int(input(f"Ingrese la capacidad de personas que caben en el bus:"))
bus_1 = Bus(bus_capacity)
while True:
    name=input(f"Ingrese el nombre del pasajero o salir para terminar:").strip()
    if name.lower() == "salir": 
            break
    nueva_persona = Person(name)
    subio = bus_1.accept_passenger(nueva_persona)
    if subio:
        ultimo=bus_1.passengers[-1]
        available_capacity = bus_1.max_passenger - len(bus_1.passengers)
        print(f"Ultimo Pasajero: {ultimo.name}")
        print(f"Capacidad Disponible: {available_capacity} pasajeros")
    else:
         decision = input("Desea bajar un pasajero? (s/n)").strip().lower()
         if decision == 's':
            person_getting_off = input("Ingrese el nombre del pasajero que se bajará:").strip()
            bus_1.let_passenger_off(person_getting_off)
            for i, p in enumerate (bus_1.passengers, start =1):
                    print(f"{i}. Nombre: {p.name} ")
            print(f"Total de personas en el bus: {len(bus_1.passengers)}")
print("""
---------------------------Lista Final de Pasajeros----------------------------------

""")
if not bus_1.passengers:
     print("El bus esta vacío")
else:
    for i, p in enumerate (bus_1.passengers, start =1):
        print(f"{i}. Nombre: {p.name}")
    print(f"Total de personas en el bus: {len(bus_1.passengers)}")
    print(f"Ocupación del bus {(len(bus_1.passengers)/bus_1.max_passenger)*100}%")
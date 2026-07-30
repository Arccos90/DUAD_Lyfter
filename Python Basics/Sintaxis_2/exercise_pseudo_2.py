#este programa convierte el tiempo de segundos a minutos
print("-------Convertidor de tiempo--------")
seconds = int(input("Ingrese el tiempo en segundos: "))
minutes = seconds / 60
if seconds < 600:
    print("Faltan:", 600 - seconds, "segundos para llegar a los 10 minutos  "
          "o", (600 - seconds) / 60, "minutos")
if seconds == 600:
    print("Igual a 10 minutos")
elif seconds > 600:
    print("Mayor a 10 minutos")
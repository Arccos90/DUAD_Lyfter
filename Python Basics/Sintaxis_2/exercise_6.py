#Este programa es un convertidor  de grados Celsius a Fahrenheit y Kelvin
print("-------Convertidor de grados Celsius a Fahrenheit y Kelvin--------")
celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15
print(f"La temperatura en grados Fahrenheit es: {fahrenheit}") #quería experimentar con F-strings   
print("La temperatura en grados Kelvin es: ", kelvin)
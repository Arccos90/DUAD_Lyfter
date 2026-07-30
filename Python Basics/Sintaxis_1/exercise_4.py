#Generador del número más alto
print("-------Generador del número más alto--------")
name = input("Ingrese su nombre: ")
number_1 = float(input("Ingrese el primer número: "))
number_2 = float(input("Ingrese el segundo número: "))
number_3 = float(input("Ingrese el tercer número: "))
highest_number = max(number_1, number_2, number_3) #La función max() devuelve el valor máximo entre los argumentos que se le pasan
print(f"{name}, el número más alto entre {number_1}, {number_2} y {number_3} es: {highest_number}")
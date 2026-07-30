#Generador de nùmeros aleatorios
print("-------Generador de números aleatorios--------")
import random
name = input("Ingrese su nombre: ")
random_number = random.randint(1, 10) #Genera un número aleatorio entre 1 y 10
input_number = int(input("Adivina el número entre 1 y 10: "))
while input_number != random_number:
    if input_number < random_number:
        print("¡Demasiado bajo! Intenta de nuevo.")
    else:
        print("¡Demasiado alto! Intenta de nuevo.")
    input_number = int(input("Adivina el número entre 1 y 10: "))
if input_number == random_number:
    print(f"¡Felicidades {name}! Has adivinado el número correcto: {random_number}")
#Este programa es un generador de números aleatorios
print("-------Generador de números aleatorios--------")
import random
random_number = random.randint(1, 10)
number = int(input("Adivine un número del 1 al 10: "))
while number != random_number:
    number = int(input("¡Inténtalo de nuevo! Adivina un número del 1 al 10: "))
print("¡Felicidades! Has adivinado el número aleatorio.")   
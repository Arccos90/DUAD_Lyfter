#Este programa es un multiplier de números
print("-------Multiplicador de números--------")    
number = int(input("Ingrese un número del 1 al 10: "))
multiplier = 1
while multiplier <= 12:
    result = number * multiplier
    print(f"{number} x {multiplier} = {result}")
    multiplier = multiplier + 1
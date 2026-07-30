# Este programa suma números que den 30
print("-------Sumador de números que den 30--------")
number1 = int(input("Ingrese el primer número: "))
number2 = int(input("Ingrese el segundo número: "))
number3 = int(input("Ingrese el tercer número: "))
sum = number1 + number2 + number3
if sum == 30:
    print("Correcto, la suma de los números es 30.")
elif number1 == 30:
    print("Correcto, el número 1 es igual a 30.")
elif number2 == 30:
    print("Correcto, el número 2 es igual a 30.")
elif number3 == 30:
    print("Correcto, el número 3 es igual a 30.")
else:
    print("Incorrecto, la suma de los números no es 30.")
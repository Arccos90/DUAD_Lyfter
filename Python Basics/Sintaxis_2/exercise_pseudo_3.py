#esto es un sumador de números
print("-------Sumador de números--------")
number = int(input("Ingrese un número: "))
counter = 1
sum = 0
while counter <= number:
    sum = sum + counter
    counter = counter + 1
print("La suma de los números del 1 al", number, "es:", sum)
print("--------Ejercicio 2 Iteraciones--------")
my_string="Pizza con piña"
counter=len(my_string)-1 # ¿Por qué -1? Porque el índice de la última letra es igual a la longitud del string menos 1, ya que el conteo de índices comienza en 0. Por ejemplo, si el string tiene una longitud de 5, los índices van de 0 a 4, por lo que el último índice es 4, que es igual a la longitud del string (5) menos 1.
print(counter)
print("-----primera forma de hacerlo-----") #esta fue el primer camino que intente sin ayuda, pero no lograba hacerlo por que no entendía la logitud del string, pero luego de entenderlo pude hacerlo con un while, aunque no se si es la mejor forma de hacerlo, pero me funcionó.
while counter>=0:
    print(my_string[counter])
    counter-=1 

print ("--------segunda forma de hacerlo--------")

for char in range(len(my_string)-1,-1,-1): #esta es otra forma que encontré de hacerlo utilizando range
    print(my_string[char])
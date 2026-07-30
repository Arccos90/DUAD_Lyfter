print("--------Ejercicio 4 Iteraciones--------")
 #esta es una forma mejorada de hacerlo utilizando list comprehension, ya que es más fácil de entender y no es necesario utilizar pop para eliminar los elementos, pero me funcionó la forma anterior.
my_list=[1,2,3,4,5,6,7,8,9]
pair_numbers=[num for num in my_list if num % 2 == 0]
no_pair_numbers=[num for num in my_list if num % 2 != 0]
print("Números pares:", pair_numbers)
print("Números impares:", no_pair_numbers)  
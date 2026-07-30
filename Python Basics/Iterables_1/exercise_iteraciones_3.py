print("--------Ejercicio 3 Iteraciones--------")
my_list=[4,3,6,1,7]
first_char=0
first_deleted_char=my_list.pop(first_char)
last_char=len(my_list)-1
last_deleted_char=my_list.pop(last_char) #esta es una forma de eliminar el primer y último elemento de la lista utilizando pop, pero no se si es la mejor forma de hacerlo, ya que no se si es correcto eliminar ambos elementos en una sola línea de código, pero me funcionó.
print(f"Primer elemento eliminado: {first_deleted_char}")
print(f"Último elemento eliminado: {last_deleted_char}")
my_list.append(first_deleted_char) #esta es una forma de agregar el primer elemento eliminado al final de la lista utilizando append, pero no se si es la mejor forma de hacerlo, ya que no se si es correcto agregar el elemento eliminado al final de la lista, pero me funcionó.
print("Lista después de agregar el primer elemento eliminado al final:", my_list)
my_list.insert(0,last_deleted_char) #esta es una forma de agregar el último elemento
print("Lista después de agregar el último elemento eliminado al principio:", my_list)
#Tuve problemas ya que al eliminar el primer elemento tuve que modificar el orden de los elementos, ya que el tamaño de la lista se redujo y el índice del último elemento cambió, pero luego de entenderlo pude solucionarlo utilizando pop para eliminar los elementos y luego agregarlos nuevamente a la lista utilizando append e insert, aunque no se si es la mejor forma de hacerlo, pero me funcionó.
print("-----forma mejorada de hacerlo, devolverá los datos a su posición original-----") #esta es una forma mejorada de hacerlo utilizando slicing, ya que es más fácil de entender y no es necesario utilizar pop para eliminar los elementos, pero me funcionó la forma anterior.
first=my_list[0]
last=my_list[-1]
first_value=my_list.pop(0) #esta es una forma de eliminar el primer elemento de la lista utilizando pop, pero no se si es la mejor forma de hacerlo, ya que no se si es correcto eliminar el elemento en una sola línea de código, pero me funcionó.
last_value=my_list.pop(-1) #esta es una forma de eliminar el último elemento de
my_list.append(first_value) #esta es una forma de agregar el primer elemento eliminado al final de la lista utilizando append, pero no se si es la mejor forma de hacerlo, ya que no se si es correcto agregar el elemento eliminado al final de la lista, pero me funcionó.
my_list.insert(0,last_value) 
print("Lista después de devolver los datos a su posición original:", my_list)

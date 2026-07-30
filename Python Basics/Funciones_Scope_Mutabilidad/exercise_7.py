"Exercise 7: Funciones, Scope y Mutables"
def prime_detector (prime_number):

     if prime_number <= 1:
         return False
     else:
            for divisor in range (2, prime_number):
                 if prime_number % divisor == 0:
                    return False
            return True

counter_numbers = int(input("¿Cuantos números desea ingresar?:"))
my_list = []
counter = 0
numbers = 0
no_prime_list = []
prime_list = []
while counter < counter_numbers:
    counter = counter + 1
    numbers = int(input("Por favor ingrese un número " + str(counter) + ": ")) #
    my_list.append(numbers)
    
for char in my_list:
    if prime_detector(char):
            prime_list.append(char)
    else:  
            no_prime_list.append(char)    
print("números ingresados:", my_list)
print ("Lista de primos:", prime_list )
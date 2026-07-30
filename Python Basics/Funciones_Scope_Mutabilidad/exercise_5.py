"Exercise 5: Funciones, Scope y Mutables"


def upper_letters  (my_string):
   #upper_list =[] , Encuentra las mayusculas y las mete en una lista
     upper_counter = 0
     for char in my_string:
      if char.isupper():
        #upper_list.append(char), Aqui acumularía las mayusculas encontradas
        upper_counter = upper_counter + 1
     return upper_counter

def lower_letters (my_string):
    #lower_list = []
     lower_counter = 0
     for char in my_string:
      if char.islower():
        #lower_list.append(char)
        lower_counter = lower_counter + 1
     return lower_counter
    
def main():
    original_text =input("Ingrese una frase:") # El valor de la variable original_text, se usa como el valor para la función reverse_string
    final_count_uppers = upper_letters(original_text)                   
    final_count_lowers = lower_letters (original_text)
    print(f"There are {final_count_uppers} upper cases,and {final_count_lowers} lower cases")

main()
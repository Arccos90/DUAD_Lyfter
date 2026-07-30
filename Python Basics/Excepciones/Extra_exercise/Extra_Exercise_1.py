print("--------------------------Extra_Exercise_1: Exceptions-------------------------------------")


def name_input():
    while True:
        try:
            name = str(input(f"Ingrese su nombre: "))
          #inclui esta seccion por que encontre que puedo escribir cosas como D4niel, y el programa lo aceptaria.
            char_check = False
            for char in name:
                if char.isdigit():
                    char_check = True
                    raise ValueError
        except ValueError as ex:
            print("!El nombre no puede ser o contener números!, Intentelo de nuevo")
            continue
        return name
 


def age_input():
    while True:
        try:
            age = int(input("Ingrese su edad: "))
            if age < 0 or age > 120:
                
                raise ValueError()
        except ValueError as ex:
            print("La edad no puede tener letras y debe ser mayor que 0 y menor a 120")
            continue
        return age


def main():
    name_str=name_input()
    age_int= age_input()
    print(f"Hola {name_str}, su edad es {age_int} años")
   

if __name__ == '__main__':
    main()

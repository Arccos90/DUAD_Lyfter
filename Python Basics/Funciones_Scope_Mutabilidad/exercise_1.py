"--------exercise 1: Funciones, Scope y Mutables--------"

def print_text_2():
    location = int(input("Ingrese el número de la sede del mundial (1: Mexico, 2: Estados Unidos, 3: Canada): "))
    if location == 1:
        print("La sede del mundial es Mexico")
    elif location == 2:
        print("La sede del mundial es Estados Unidos")
    elif location == 3:
        print("La sede del mundial es Canada")
    else:
        print("Número de sede no válido")

def print_text_1():
    print("Copa del mundo 2026")
    print_text_2()

print_text_1()

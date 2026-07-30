import sys #investigué una manera de cerrar el programa por completo desde el menú
def add (num1,num2):
        result = num1 + num2
        return result
def rest (num1,num2):
        result = num1 - num2
        return result
def multiplier (num1,num2):
        result = num1 * num2
        return result
def divisor(num1,num2):
     result = num1/num2
     return result

def main():
    print("--------Calculadora por linea de comando---------------")
    current = 0
    while True:
        try:
            print(f"El número actual es: {current}")
            if current == 0:
                
                current = float(input("Ingrese un número:"))
            operation_number = float(input("Selecciones la operación que desea ejecutar: (1)-Sumar / (2)-restar / (3)-multiplicar / (4)-División /(5)-Borrar /(6)-Cerrar la calculadora:"))
            if operation_number == 6:
                 sys.exit("La calculadora ha sido cerrada, nos vemos luego!")
            if operation_number==5:
                    print ("Se ha borrado la operación")
                    current = 0
                    continue
        
            number_2 = float(input("Ingrese el segundo número:"))

            if operation_number ==1:
                current  = add(current,number_2)
        
            elif operation_number ==2:
                current = rest(current,number_2)
        
            elif operation_number ==3:
                current = multiplier(current,number_2)
            elif operation_number ==4:
                current = divisor(current,number_2)
            else:
                print ("Operación no válida!")
            print(f"El resultado es: {current}")        
        except ValueError as ex:
            print (f"An unexpected error ocurred on main fuction: {ex}")
        except ZeroDivisionError:
            print("Error: No se puede dividir entre cero.")


main()

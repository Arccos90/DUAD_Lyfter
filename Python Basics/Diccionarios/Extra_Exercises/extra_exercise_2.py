print (f"---------------------Extra_Exercise_#2-------------------------")
def main():
    while True:
        print ("-----------------------Menú principal--------------------------")
        print ("(1)-Ingresar un nuevo colaborador" )
        print ("(2)-Ejecutar un resumen por departamento")
        print ("(3)-Salir")
        
        try:
            menu_option = int(input(f"Elija que opcion desea realizar: "))
        except ValueError:
            print (f"Ingrese una opción valida")
            continue

        if menu_option == 1:
                new_employee={}
                name = str(input(f"Ingrese el nombre del colaborador: "))
                email = str(input(f"Ingrese el mail del colaborador: "))
                department = str(input(f"Ingrese el departamento del colaborador: "))
                new_employee ['name']= name
                new_employee ['email'] = email
                new_employee ['department'] = department
                employees.append(new_employee)
                counter = len(employees)
                print (f"Ha ingresado {counter} colaboradores")
                print (f"Colaboradores ingresados: {employees}")
        elif menu_option == 2:
                    report = {}
                    for employee in employees:
                        print (f"{employee}") 
                        depart_sum = employee ['department']
                        employee_sum = employee ['name']
                        if depart_sum not in report:
                            report [depart_sum] = []
                        report[depart_sum].append(employee_sum)
                    print (f"Estos son los colaboradores por departamento: {report}")     
        elif menu_option == 3:
              print ("Cerrando el programa. !Nos vemos pronto!")
              break
        else:
              print("Ingrese una opcion válida:")


employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]
counter = 0
menu_option = 0
main()
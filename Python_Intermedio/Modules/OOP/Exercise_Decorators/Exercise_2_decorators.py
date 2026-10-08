"------------------------Exercise_2: Decorators----------------------"

def number_validation (func):
    def wrapper (*args,**kwargs):
        print(f"estos son los kwargs: {kwargs}")
        print(f"estos son los args: {args}")
        all_values = list(args) + list(kwargs.values())
        for values in all_values:
            if type (values) not in (int, float):
                raise TypeError(f"{values} no es un número")
        result = func(*args,**kwargs)
        print(f"Validador de función {result}")
        return result
    return wrapper

@number_validation
def area (base:float, height:float):
        area = base * height
        print(f"El area del rectangulo es: {area}")
        return round(area,2)

@number_validation
def perimeter (base:float, height:float):
        perimeter = 2*(base+height)
        print(f"El perimetro del rectangulo es {perimeter}")
        return round(perimeter, 2)
    
print("-------PRUEBAS------")
print("Prueba 1: valores númericos")
try:
    perimeter (10,5)
    area (base=50,height=60)
except TypeError as error:
     print(f"Error inesperado {error}")
    
print("Pruebas 2: Valores no numericos (args)")
try:
     
    area (20,"cuarenta")
    perimeter("cinco", "tres")
except TypeError as error:
     print(f"Exepción args identificada: {error}")

print("Pruebas 3: Valores no numericos (kwargs)")
try:
    area (base = "dos", height= 20)
except TypeError as error:
    print(f"Exepción kwargs identificada: {error}")

print("Pruebas 4: Valores no numericos combinados")
try:
    perimeter(2, height= 20)
    area(2, height="veinte")
except TypeError as error:
    print(f"Exepción combinada identificada: {error}")
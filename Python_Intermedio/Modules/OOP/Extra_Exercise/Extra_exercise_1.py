print("----------------------Extra exercise 1-----------------------------")
import math
class Rectangle:
    def __init__(self, width: float, height:float):
        self.width = width
        self.height = height

    def get_area (self):
        area = self.width*self.height
        return area

    def get_perimeter (self):
        perimeter = self.width*2 + self.height*2
        return perimeter

while True:
    
    try:
        width = float(input("Ingrese el valor del ancho del rectangulo:"))
        height = float(input("Ingrese el valor del alto del rectangulo:"))
        if width >0 and height > 0:
            break
        else:
            print("!Error! Debe ingresar un número mayor a cero!")
    except ValueError:
                print("!Error! Debe ingresar un número válido!")

rectagule_1 = Rectangle(width,height)
area = rectagule_1.get_area ()
perimeter = rectagule_1.get_perimeter()

print(f"El area del rectangulo es {area}")
print(f"El perímetro rectangulo es {perimeter}")
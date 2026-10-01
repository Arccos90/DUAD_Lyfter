"------------------------Exercise 2 4Pillar OOP--------------------------"
import math
from abc import ABC, abstractmethod
class Shape (ABC):
    @abstractmethod
    def calculate_perimeter (self):
        pass
    @abstractmethod
    def calculate_area (self):
        pass

class Circle (Shape):
    def __init__(self,radius:float):
        self.radius=radius

    def calculate_area(self) -> float:
        area = (self.radius**2)*math.pi
        print(f"El area del circulo es: {area:.2f}")
        return area

    def calculate_perimeter(self) -> float:
        perimeter = (self.radius)*2*math.pi
        print(f"El perimetro del circulo es: {perimeter:.2f}")
        return perimeter

class Square (Shape):
    def __init__(self, side:float):
        self.side = side

    def calculate_area(self) -> float:
        area = self.side*self.side
        print(f"El area del cuadrado es: {area:.2f}")
        return area

    def calculate_perimeter(self):
        perimeter = self.side*4
        print(f"El perimetro del cuadrado es: {perimeter: .2f}")
        return

class Rectangle (Shape):
    def __init__(self, side_a:float, side_b:float):
        self.side_a = side_a
        self.side_b = side_b

    def calculate_area(self)-> float:
        area = self.side_a * self.side_b
        print(f"El area del rectangulo es: {area:.2f}")
        return area

    def calculate_perimeter(self)->float:
        perimeter = self.side_a*2 + self.side_b*2
        print(f"El perimetro del rectangulo es: {perimeter:.2f}")
        return perimeter

menu = int(input("¿Con que figura desea trabajar? 1-Circulo, 2-Cuadrado, 3-Rectangulo ó 4-Salir: "))
if menu == 1:
    radius = float(input("Ingrese el radio del circulo: "))
    shape = Circle(radius)
    shape.calculate_area()
    shape.calculate_perimeter()
elif menu == 2:
    side=int(input("Ingrese la medida del lado del cuadrado: "))
    shape = Square(side)
    shape.calculate_area ()
    shape.calculate_perimeter()
elif menu == 3:
    side_a=int(input("Ingrese la medida de la base del rectangulo: "))
    side_b=int(input("Ingrese la medida de la altura del rectangulo: "))
    shape = Rectangle(side_a,side_b)
    shape.calculate_area ()
    shape.calculate_perimeter()
elif menu == 4:
    quit()

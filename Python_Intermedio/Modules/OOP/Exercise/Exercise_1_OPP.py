import math
class Circle:
    def __init__ (self, radius:float):
        self.radius = radius
       
    def get_area(self):
        area = (self.radius**2)*math.pi
        return area
        


radio = float(input("Ingrese un valor de radio: "))
circle_1 = Circle(radio)
area =circle_1.get_area()
print(f"El area del circulo es: {area:.2f}") #:.2f led me show only 2 decimals

        
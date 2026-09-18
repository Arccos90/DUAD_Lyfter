import math
class Circle:
    radius = 0
       
    def get_area(self, radius):
        self.area = (radius**2)*math.pi
        print(f"El area del circulo es {self.area}")
        return


area_circle_1 = Circle()
radio = int(input(f"Ingrese un valor de radio: "))
area_circle_1.get_area(radio)

        
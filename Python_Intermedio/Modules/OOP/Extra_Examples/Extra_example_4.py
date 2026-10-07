class Rectangle:
    def __init__(self, base:float,altura:float):
        self.base = base
        self.altura = altura

    @property
    def area (self)-> float:
        area = self.base * self.altura
        return round(area,2)

    @property
    def perimeter (self)->float:
        perimeter = 2*(self.base+self.altura)
        return round(perimeter, 2)

base = float(input("Ingrese la base del rectangulo: "))
altura = float(input("Ingrese la altura del rectangulo: "))
rectangulo = Rectangle (base,altura)
print(rectangulo.area)
print(f"El perimetro del rectangulo es: {rectangulo.perimeter}")
rectangulo.base = 2
rectangulo.altura = 2
print(f"El perimetro del rectangulo es: {rectangulo.perimeter}")
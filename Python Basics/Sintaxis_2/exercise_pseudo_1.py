# este programa muestra los decuentos según el precio
print("-------Calculadora de descuentos--------")
price = float(input("Ingrese el precio del producto: "))
discount = 0
if price >= 100:
    discount = price * 0.1
if price < 100: 
    discount = price * 0.02
print("El descuento es de:", discount)
print("el precio final es de:", price - discount)
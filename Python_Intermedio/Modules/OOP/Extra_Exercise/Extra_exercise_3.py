import math

class Product :
    def __init__(self, name:str, price:float, quantity:int):
        self.name = name
        self.price = price
        self.quantity = quantity
        

class Inventory:
    def __init__(self):
        self.stock_list = []
        self.counter = 0
    def add_product (self, product: Product):
        add_product = self.stock_list.append (product)
        print(f"se ha agregado el producto: {product.name}")
        self.show_products()
       
    def show_products (self):
        if not self.stock_list:
            print("El inventario está vacío")
            return
        print("--------------Inventario actual---------------")
        for i, item in enumerate (self.stock_list, start=1):
            sub_total = item.price*item.quantity
            print(f"{i} -- {item.name}__price: ${item.price}___ Qty:{item.quantity} und | Inventario Acumulado: ${sub_total}")
        self.show_total_stock ()

    def show_total_stock (self):
        total = 0
        for product in self.stock_list:
            total += product.price*product.quantity
        print(f"total inventario: $ {total}")
        return total

inventory = Inventory()
while True:
    product_name = str(input("Ingrese el nombre del producto:")).upper()
    product_price = int(input("Ingrese el precio del producto:"))
    product_qty = int(input("¿Cuantas unidades va ingresar?"))
    product_1 = Product(product_name, product_price,product_qty)
    print(product_1.name)
    save_option= input("¿Desea guardar el producto en el inventario? (S/N)").strip().lower()
    if save_option.lower() == "s":
        save_product = inventory.add_product(product_1)
        next_option = input("¿Desea ingresar otro item? (S/N)").strip().lower()
        if next_option == "n":
            print("Gracias por usar nuestro programa de gestión de inventario!!")
            break
        elif next_option == "s":
            continue
        
    elif save_product== "n":
        print("Gracias por usar nuestro programa de gestión de inventario!!")
        break


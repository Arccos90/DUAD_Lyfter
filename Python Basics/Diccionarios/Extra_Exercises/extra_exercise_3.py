print (f"---------------------Extra_Exercise_#3-------------------------")
products = [
    {"name": "Monitor", "category": "Electrónica", "price": 200},
    {"name": "Teclado", "category": "Electrónica", "price": 50},
    {"name": "Silla", "category": "Muebles", "price": 120},
    {"name": "Mesa", "category": "Muebles", "price": 180},
    {"name": "Mouse", "category": "Electrónica", "price": 25},
]
counter = 0
new_product_list = {}
for items in products:
    #print(f"{items}") #Valido si logré extraer el diccionario de la lista
    category = items ['category']
    price = items['price']
    if category not in new_product_list:
        new_product_list[category] = []
    new_product_list [category].append(price) 

    
print(f"Este es el reporte por categoría:")
print(f"{new_product_list}")

total_by_category = {}

for category, prices in new_product_list.items():
        total = sum(prices)
        total_by_category[category]=total

print(f"Este es el reporte por categoría sumado:")
print(f"{total_by_category}")
#------------------Actions-----------------------------
from finance_manager import Category, Income, Expense, AdmFinance
from datetime import datetime
from data_percistence import save_data

def validate_amount(amount_str: str)-> float:
    clean_amount_str = amount_str.replace(",",".")
    amount = float(clean_amount_str)
    if amount <= 0:
        raise ValueError("El monto debe ser mayor a cero")
    return amount

def process_new_category(manager: AdmFinance, name:str, color: str):
    if not name.strip():
        raise ValueError("El nombre de la categoría no debe estar vacío")
    if name in manager.categories:
        raise ValueError("Esta categoria ya existe")

    new_category = Category(name.strip(),color)
    manager.categories[new_category.name] = new_category
    save_data(manager)
    return new_category

def process_new_transaction(manager:AdmFinance, type:str, title:str, amount_string:str, cat_name:str):
    if not manager.categories:
        print("No hay categorias disponibles, crea una categoria!")
    if not title.strip():
        print("El título no puede estar vacío")
    if not cat_name or cat_name not in manager.categories:
        raise ValueError("Se debe seleccionar una categoría válida!")
    amount = validate_amount(amount_string)
    category_target = manager.categories[cat_name]
    actual_date= datetime.now().strftime("%d/%m/%Y")

    if type == "Ingreso":
        transaction = Income(category_target, title.strip(), amount, actual_date)
    else:
        transaction = Expense(category_target, title.strip(),amount,actual_date)

    manager.add_new_transaction(transaction)
    save_data(manager)
    return transaction